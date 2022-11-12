from django.core.management.base import BaseCommand

from scraper.tasks import crawler #create_workers, crawl

class Command(BaseCommand):
    help = 'Testing Celery Task'

    def handle(self, *args, **options):
        try:
            self.stdout.write(self.style.WARNING('Calling Celery shared task.. '))
            # create_workers()
            # crawl()
            crawler()
            self.stdout.write(self.style.SUCCESS('Done'))


        except Exception as e:
            self.stdout.write(self.style.ERROR("ERROR:{}".format(e)))