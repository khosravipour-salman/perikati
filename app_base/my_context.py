from app_base.custom_admin import admin_site
from django.urls import reverse


def get_app_list(request):  # we have comment out it in footer
    if request.path.startswith(reverse('admin:index')):
        return {'APP_LIST': admin_site.get_app_list(request)}
    else:  # none admin pages
        return {'APP_LIST': []}
