from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("register/", views.registerPage, name="register"),
    path("login/", views.loginPage, name = "login"),
    path("logout/", views.logoutPage, name = "logout"),

    path("", views.index, name="index"),

    path("<int:userInputId>", views.showUserInputDetails, name = "showUserInputDetails"),
    path("saveUserInput/", views.saveUserInput, name = "saveUserInput")
]
# Serve static files with Django. Normally this is for development purposes.
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
