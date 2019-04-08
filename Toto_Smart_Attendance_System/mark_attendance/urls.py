from django.conf.urls import url

from . import views


app_name = 'mark_attendance'

urlpatterns = [
    url(r'^', views.mark_attendance, name="mark_attendance"),
]
