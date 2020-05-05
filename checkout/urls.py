from django.conf.urls import url
from .views import check_out

urlpatterns = [
    url(r'^$', check_out, name=check_out),
]
