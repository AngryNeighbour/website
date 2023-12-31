from django.urls import include, path
from . import views

urlpatterns = [
    path("accounts/", include("django.contrib.auth.urls")),
    path("register/", views.Register.as_view(), name='register'),
    path("password_reset/", views.Password_reset_view1.as_view(), name="password_reset"),
    path("reset/<uidb64>/<token>/",views.PasswordResetConfirmView_1.as_view(),name="password_reset_confirm",),
    path("reset/done/",views.PasswordResetCompleteView_1.as_view(),name="password_reset_complete",),
    path("password_reset/done/",views.PasswordResetDoneView_1.as_view(),name="password_reset_done",),


    path("", views.index, name="index"),
    path("edit/", views.edit, name="edit"),
    path("save_edit", views.save_edit, name="save_edit"),
    path("poem/<str:title>", views.poem, name="poem"),
    path("new_poem/", views.new_poem, name="new_poem"),
    path("delete_poem/<str:title>", views.delete_poem, name="delete_poem"),

    #path("profile/", views.view_profile, name="view_profile"),
    path("profile/", views.ViewProfile.as_view(), name="view_profile"),
    path("profile/edit/", views.EditProfile.as_view(), name="edit_profile"),
    #path("profile/edit/", views.edit_profile, name="edit_profile"),



    path("test/", views.test, name="test"),
    path("about/", views.about, name="about"),


]
