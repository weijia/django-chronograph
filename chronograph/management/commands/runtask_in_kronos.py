from django.core.management.base import BaseCommand, CommandError
from django.utils.module_loading import autodiscover_modules
from kronos import registry


class Command(BaseCommand):
    help = 'Run task in kronos'

    def add_arguments(self, parser):
        parser.add_argument('task', nargs='?', type=str)

    def handle(self, *args, **options):
        autodiscover_modules('cron')

        task_name = options.get('task')

        for task in registry:
            if task.name == task_name:
                if task.function:
                    return task.function()
                else:
                    raise CommandError('This is a django command. You have '
                                       'to run it via python manage.py {0}'
                                       .format(task_name))
        raise CommandError('Task \'%s\' not found' % task_name)
