import logging

from django.core.management.base import BaseCommand


class Command(BaseCommand):
    def handle(*args, **kwargs):
        ping_handler = logging.handlers.HTTPHandler(
            host='morningwhale:8666',
            url='/v0/logged-event/',
        )
        logger = logging.getLogger(__name__)
        logger.addHandler(ping_handler)
        logger.warn("it's here!")
