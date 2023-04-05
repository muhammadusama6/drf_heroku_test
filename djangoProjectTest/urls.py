from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path("rollnumbers/", include('testapi.urls')),
    path('tasklist/', include('taskapi.urls'))
]
