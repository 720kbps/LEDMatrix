from django.apps import AppConfig
from TableVisualiser.logic.strip import get_strip


class TablevisualiserConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'TableVisualiser'

    def ready(self):
        get_strip()
