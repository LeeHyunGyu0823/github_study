from django.urls import path

from projectapp.views import ProjectCreateView

app_name = 'project_app'

urlpatterns = [
    path('create/', ProjectCreateView.as_view(), name='create'),

]