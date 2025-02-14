from django.urls import path
from .views import contact_form_submission

urlpatterns = [
    path("", contact_form_submission, name="contact_form"),
]
