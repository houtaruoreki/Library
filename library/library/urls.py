from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('Reader.urls')),
    path('books/', include('Book.urls', namespace='Book'))
]
