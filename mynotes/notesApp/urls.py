from django.contrib import admin
from django.urls import path, include

urlpatterns = [
	path('admin/', admin.site.urls),
	# Enter the app name in following syntax for this to work
	path('', include("notesApp.urls")),
]
