#!/bin/bash

#mkdir temp
mkdir -p /tmp/devops_celery

#comsumer
celery -A mymain worker -l info

#production
celery -A mymain beat -l info -s /tmp/devops_celery
