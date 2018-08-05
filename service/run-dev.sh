#!/usr/bin/env bash
gunicorn --reload --timeout 60 --bind 0.0.0.0:8080 'webapi.app:create_app()'
