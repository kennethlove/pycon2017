from django.core.management.base import BaseCommand, CommandError

from products import factories, models


class Command(BaseCommand):
    help = 'Generates random products'

    def add_arguments(self, parser):
        parser.add_argument('count', type=int)

        parser.add_argument(
            '--clear',
            action='store_true',
            dest='clear',
            default=False,
            help='Clear all existing products first'
        )

    def handle(self, *args, **options):
        count = options['count']
        if options['clear']:
            models.Product.objects.all().delete()
        factories.ProductFactory.create_batch(size=count)
        self.stdout.write(self.style.SUCCESS(f'Generated {count} product(s)!'))
