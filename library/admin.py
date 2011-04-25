from django.contrib import admin
from jnsqlibs.library.models import Library, Version, Dependency

admin.site.register(Library)
admin.site.register(Version)
admin.site.register(Dependency)
