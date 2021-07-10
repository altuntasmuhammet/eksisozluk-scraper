#!/bin/sh

pip3 install flower && \
celery -A altuntas flower --port=8888