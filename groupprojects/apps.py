from django.apps import AppConfig


class GroupprojectsConfig(AppConfig):
    name = 'groupprojects'

    def ready(self):
        import groupprojects.signals
