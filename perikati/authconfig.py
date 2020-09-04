# 'authconfig.py'
from django.contrib.auth.apps import AuthConfig

class CustomAuthConfig(AuthConfig):
    name = 'django.contrib.auth'
    verbose_name = 'مدیریت کاربران'
