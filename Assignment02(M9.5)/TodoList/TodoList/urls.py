from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.show_tasks, name='show_tasks'),
    path('completed_tasks/', views.show_complete_tasks, name='show_complete_tasks'),
    path('task/', include('tasks.urls')),
]