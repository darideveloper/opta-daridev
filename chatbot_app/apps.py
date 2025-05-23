from django.apps import AppConfig


class ChatbotAppConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "chatbot_app"
    verbose_name = "Demo"
    
    def ready(self):
        import chatbot_app.signals