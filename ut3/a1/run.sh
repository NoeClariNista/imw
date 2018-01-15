#!/bin/bash

source /home/alu5904/.virtualenvs/vm/bin/activate
uwsgi --ini /home/alu5904/vm/a8/uwsgi.ini
