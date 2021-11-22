from django.urls import path
from users.views import signup_view

urlpatterns = [path('registrer/', signup_view, name="registrer")
]