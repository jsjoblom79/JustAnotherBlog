from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('settings/', admin.site.urls),
    path('blog/', include('blog.urls'))
]
