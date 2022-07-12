from django.urls import path
from . import views

app_name = "users"

urlpatterns = [
    path("login/", views.LoginView.as_view(), name="login"),
    path("logout/", views.log_out, name="logout"),
    path("signup/", views.SignUpView.as_view(), name="signup"),

    # path("verify/<str:key>/", views.complete_verification, name="complete-verification"),
    path("login/google/", views.google_login, name="google-login"),
    path("login/google/callback/", views.google_callback, name="google-callback"),
    # path("login/facebook/", views.facebook_login, name="facebook-login"),
    # path("login/facebook/callback/", views.facebook_callback, name="facebook-callback"),

    path("<int:pk>/", views.UserProfileView.as_view(), name="profile"),
    path("update-profile/", views.UpdateProfileView.as_view(), name="update"),
    path("update-password/", views.PasswordChangeView.as_view(), name="password"),
    path("switch-hosting/", views.switch_hosting, name="switch-hosting"),
]
