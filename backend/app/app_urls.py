from django.urls import path, include

from .views import oauth2, RegistrationAPI, LoginAPI, UserAPI, LogoutView, GithubCallbackAPI, scan_repo

urlpatterns = [
    path('oauth2/', oauth2, name='oauth2'),
    path('auth/register/', RegistrationAPI.as_view(), name='register'),
    path('auth/user/', UserAPI.as_view(), name='user'),
    path('auth/login/', LoginAPI.as_view(), name='login'),
    path('auth/logout/', LogoutView.as_view(), name='logout'),
    path('auth/github_callback/', GithubCallbackAPI.as_view(), name='github_callback'),
    path('auth/get_repository/', scan_repo, name='repository'),
]