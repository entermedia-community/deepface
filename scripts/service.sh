#!/usr/bin/env bash
cd ../deepface/api/src

# run the service with flask - not for production purposes
# python api.py

# run the service with gunicorn - for prod purposes
gunicorn --workers=1 --timeout=3600 --bind=127.0.0.1:5000 --log-level=debug "app:create_app()"