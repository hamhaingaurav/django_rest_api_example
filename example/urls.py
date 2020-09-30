from django.urls import path
from example.views import HomeView, UserListAPIView, user_detail
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy


urlpatterns = [
    path('home/', HomeView.as_view(), name='home'),

    path('account/login/', auth_views.LoginView.as_view(template_name='login.html', redirect_authenticated_user=True), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
    # path('account/register/', auth_views.LogoutView.as_view(), name='register'),

    path('account/password-reset/', auth_views.PasswordResetView.as_view(template_name='password-reset.html', success_url = reverse_lazy('password-reset-done')), name='password-reset'),
    path('account/password-reset/done/', auth_views.PasswordResetDoneView.as_view(template_name='password-reset-done.html'), name='password-reset-done'),
    path('account/password-reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name='password-reset-confirm.html'), name='password-reset-confirm'),
    path('account/password-reset/complete/', auth_views.PasswordResetCompleteView.as_view(template_name='password-reset-complete.html'), name='password-reset-complete'),

    path('account/password-change/', auth_views.PasswordChangeView.as_view(), name='password-change'),
    path('account/password-change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password-change-done'),

    path('users/', UserListAPIView.as_view(), name='user_list_api_view'),
    path('user/<int:id>', user_detail, name='user_detail_api_view'),
]