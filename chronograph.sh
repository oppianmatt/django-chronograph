#!/bin/bash
PROJECT_PATH=$1
source $PROJECT_PATH"/../../../ve/bin/activate" && cd $PROJECT_PATH && python manage.py cron
