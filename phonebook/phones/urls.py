from django.urls import path
from . import views

app_name = 'phones'
urlpatterns = [
    path('create/', views.create_entry, name='create'),
    path('', views.show_add_entry_form, name='show-add-entry-form'),
]
