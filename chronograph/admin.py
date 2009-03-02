from django.contrib import admin
from django.http import HttpResponseRedirect, Http404
from django.conf.urls.defaults import patterns, url
from chronograph.models import Job, Log

class JobAdmin(admin.ModelAdmin):
    list_display = ('name', 'next_run', 'last_run', 'frequency', 'params', 'get_timeuntil',)
    list_filter = ('frequency', 'disabled',)
    
    fieldsets = (
        (None, {
            'fields': ('name', ('command', 'args',), 'disabled',)
        }),
        ('Frequency options', {
            'classes': ('wide',),
            'fields': ('frequency', 'params', 'next_run',)
        }),
    )
    
    def view_run_job(self, request, pk):
        try:
            job = Job.objects.get(pk=pk)
        except Job.DoesNotExist:
            raise Http404
        
        next_run = job.next_run
        job.run()
        job.next_run = next_run
        job.save()
        
        request.user.message_set.create(message='The job "%s" was run successfully.' % job)
        
        return HttpResponseRedirect(request.path + "../")
    
    def get_urls(self):
        urls = super(JobAdmin, self).get_urls()
        my_urls = patterns('',
            url(r'^(.+)/run/$', self.admin_site.admin_view(self.view_run_job), name="admin_chronograph_job_run")
        )
        return my_urls + urls

class LogAdmin(admin.ModelAdmin):
    list_display = ('job_name', 'run_date',)
    search_fields = ('stdout', 'stderr',)
    
    def job_name(self, obj):
      return obj.job.name
    job_name.short_description = 'Name'

admin.site.register(Job, JobAdmin)
admin.site.register(Log, LogAdmin)