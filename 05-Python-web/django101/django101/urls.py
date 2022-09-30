
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    #SITE_URL/tasks/ (localhost:8000/tasks/)
    path('tasks/', include('django101.tasks.urls'))
]
