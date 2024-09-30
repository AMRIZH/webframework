from django.contrib import admin
from django.urls import path, include

# Do not import views from 'mywebsite' (the project folder)
# Instead, you include the URLs of your app 'webapp'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('webapp.urls')),  # Use 'include' to link webapp's URLs
]