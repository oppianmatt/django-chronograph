# hook to find setup tools if not installed
from ez_setup import use_setuptools
use_setuptools()

from setuptools import setup, find_packages
setup(
    name = "django-chronograph",
    version = "svn-r21-git.1",
    packages = find_packages(),

    include_package_data=True,
    zip_safe=False,

    description='Django chronograph application.',
    author='Weston Nielson',
    author_email='wnielson@gmail.com',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Framework :: Django',
    ],
    
    license = "MIT",
    keywords = "django s3 build",
    url = "http://oppian.com/labs/django-build/",   # project home page, if any
)
