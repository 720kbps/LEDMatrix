from django.apps import AppConfig
from TableVisualiser.logic.strip import get_strip


class TableVisualiserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TableVisualiser'

    def ready(self):
        print('Initializing LED strip...')
        get_strip()
        print('LED strip initialized.')
