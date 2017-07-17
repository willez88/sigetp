from django.conf.urls import url, include
from django.contrib.auth import views as auth_views

urlpatterns = [

    url(r'^login/$', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    url(r'^logout/$', auth_views.LogoutView.as_view(), name='logout'),
    url(r'^reset/password_reset$', auth_views.PasswordResetView.as_view(template_name='password_reset_form.html',
        email_template_name='password_reset_email.html'),
        name='password_reset'),
    url(r'^password_reset_done', auth_views.PasswordResetDoneView.as_view(template_name='password_reset_done.html'),
        name='password_reset_done'),
    url(r'^reset/(?P<uidb64>[0-9A-Za-z_\-]+)/(?P<token>.+)/$',
        auth_views.PasswordResetConfirmView.as_view(template_name='password_reset_confirm.html'),
        name='password_reset_confirm'),
    url(r'^reset/done', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset_complete.html'),
        name='password_reset_complete'),
    url(r'^cambiar-clave$', auth_views.PasswordChangeView.as_view(template_name='password_change_form.html'), name='password_change'),
    url(r'^cambiar-clave-hecho$', auth_views.PasswordChangeDoneView.as_view(template_name='password_change_done.html'), name='password_change_done'),
]
