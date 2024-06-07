from django.apps import AppConfig


class ProduitsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'PRODUITS'
    def ready(self) :
        import PRODUITS.signals
