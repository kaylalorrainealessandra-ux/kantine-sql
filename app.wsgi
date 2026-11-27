import sys
import site
import os

site.addsitedir('/var/www/amandus/env/lib/python3.13/site-packages')

sys.path.insert(0, '/var/www/amandus')

os.chdir('/var/www/amandus')

os.environ['VIRTUAL_ENV'] = '/var/www/amandus/env'
os.environ['PATH'] = '/var/www/amandus/env/bin:' + os.environ['PATH']

from app import app as application
