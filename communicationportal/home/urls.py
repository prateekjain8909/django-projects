from django.conf.urls import url
from . import views
from django.contrib.auth.views import (
    LoginView,
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView,
    PasswordResetForm
    )
urlpatterns = [
    url(r"login/$", LoginView.as_view(template_name="login.html"), name="login"),
    url(r"logout/$", LogoutView.as_view(template_name="logout.html"), name="logout"),
    url(r"reset-password/$", PasswordResetView.as_view(),name="reset_password"),
    url(r"reset-password/done/$", PasswordResetDoneView.as_view(),name="password_reset_done"),
    url(r"reset-password/complete/$", PasswordResetCompleteView.as_view(),name="password_reset_complete"),
    url(r"reset-password/confirm/(?P<uidb64>[0-9a-zA-Z]+)-(?P<token>.+)/$", PasswordResetConfirmView.as_view(),name="password_reset_confirm"),
    url(r"home/$", views.home, name="home"),    
    url(r"videos/add/$", views.add_videos,name="add_videos"),
    url(r"products/add/$", views.add_products,name="add_products"),
    url(r"products/details/([0-9]+)/$", views.product_details,name="product_details"),
    url(r"products/$", views.products,name="products"),
    url(r"real-estate/add/$", views.add_real_estate,name="add_real_estate"),
    url(r"real-estate/details/([0-9]+)/$", views.real_estate_details,name="real-estate_details"),
    url(r"real-estate/$", views.real_estate,name="real_estate"),
    url(r"videos/$", views.videos,name="videos"),
    url(r"profile/$", views.view_profile,name="view_profile"),
    url(r"profile/edit/$", views.edit_profile,name="edit_profile"),
    url(r"profile/change-password/$", views.change_password,name="change_password"),
    url(r"register/$", views.register,name="register"),
    url(r"profile/chat/$", views.chat_view,name="chat"),
    # url(r"legal/$", views.legal,name="legal"),
    # url(r"category/$", views.category,name="category"),
]
