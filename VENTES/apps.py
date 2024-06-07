from django.apps import AppConfig


class VentesConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'VENTES'
    def ready(self) -> None:
        import VENTES.signals
