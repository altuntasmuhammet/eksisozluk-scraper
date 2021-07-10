#!/bin/sh

celery -A altuntas beat -l info --scheduler django_celery_beat.schedulers:DatabaseScheduler