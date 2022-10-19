#!/usr/bin/env python
#
# To enable this hook, rename this file to hook_started.py.
#
# It's a way to check if the environment is ready for the test.
#  * check if a port is listening before executing the test
#  * check if a database in postgresql is up and mounted
#

# mysql mount a temporary database first, then mount a second one
# The server answer for the first one on port 3306
#
# I have to find a way to replace this sleep by a check
from time import sleep

from django.core.management import call_command
from django.core.wsgi import get_wsgi_application

application = get_wsgi_application()
sleep(14)

call_command('makemigrations', verbosity=0)
call_command('migrate', verbosity=0)
