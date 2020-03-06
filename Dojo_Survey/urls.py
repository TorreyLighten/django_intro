from django.urls import path, include

urlpatterns = [
    path('', include('Survey_app.urls')),
]
