
"""
Django command wait for the database to be available
"""

import time
from psycopg2 import OperationalError as Psycopg20pError
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    ''''Django Cammand for database'''
    def handle(self, *args,**options):
        '''Entry point for Cammand'''
        self.stdout.write('Waiting for database')
        db_up = False
        while db_up is False:
            try:
                self.check(databases= ['default'])
                db_up = True
            except:
                self.stdout.write('Waiting for database unavailable,')
                time.sleep(1)
        self.stdout.write(self.style.SUCCESS('Database is available'))
        
