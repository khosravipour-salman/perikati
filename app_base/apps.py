from django.apps import AppConfig


class AppBaseConfig(AppConfig):
    name = 'app_base'
    verbose_name='پیش فاکتور ها'

    def ready(self):
        from . import custom_admin
