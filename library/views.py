from libs.library.models import *
from django.shortcuts import get_object_or_404, render_to_response
from django.http import HttpResponse

def list_libraries(request):
    libs = Library.objects.all()
    return render_to_response("library/list.html", {'libraries': libs})

def show_library(request, library):
    l = get_object_or_404(Library, slug = library)
    return render_to_response("library/show.html", {'library': l})

def use_library(request, library, version = None):
    l = get_object_or_404(Library, slug = library)
    version is None and version = l.current_version
    v = l.version_set.get(version__exact = version)
    return HttpResponse(v.data, mimetype = l.mimetype)
