from django.contrib import admin
from django.urls import path

from menu.views import get_main_page


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", get_main_page, name="main_page")
]
