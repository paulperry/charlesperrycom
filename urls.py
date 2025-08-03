from django.urls import path, include, re_path
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import RedirectView
from django.http import HttpResponse, Http404, FileResponse
from sculpture.views import index
import os
import mimetypes

def favicon_view(request):
    favicon_path = os.path.join(settings.BASE_DIR, 'favicon.ico')
    if os.path.exists(favicon_path):
        with open(favicon_path, 'rb') as f:
            return HttpResponse(f.read(), content_type='image/x-icon')
    else:
        # Try media favicon
        favicon_path = os.path.join(settings.MEDIA_ROOT, 'favicon.ico')
        if os.path.exists(favicon_path):
            with open(favicon_path, 'rb') as f:
                return HttpResponse(f.read(), content_type='image/x-icon')
    return HttpResponse(status=404)

def serve_media(request, path):
    """Custom media file serving for production"""
    file_path = os.path.join(settings.MEDIA_ROOT, path)
    if os.path.exists(file_path) and os.path.isfile(file_path):
        content_type, _ = mimetypes.guess_type(file_path)
        return FileResponse(open(file_path, 'rb'), content_type=content_type)
    raise Http404("Media file not found")


urlpatterns = [
    path('', index, name='home'),
    path('favicon.ico', favicon_view, name='favicon'),
    path('sculpture/', include('sculpture.urls')),
    path('bio/', include('bio.urls')),
    path('puzzles/', include('puzzles.urls')),
    path('jewelry/', include('jewelry.urls')),
    path('chairs/', include('chairs.urls')),
    path('books/', include('books.urls')),
]

# Custom media file serving (works in both DEBUG and production)
urlpatterns.append(re_path(r'^media/(?P<path>.*)$', serve_media, name='media'))

# Also add the standard static serving for DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

legacy_redirects = [
    (r'^Bio\.html$', '/bio/bio'),
    (r'^bio/bio.html$', '/bio/bio'),
    (r'^eclipse/$', '/sculpture/'),
    (r'^index\.html$', '/'),
    (r'^bylocation\.html$', '/sculpture/map/'),
    (r'^sculpture/list.html$', '/sculpture/list/'),
    (r'^Ribbed\.html$', '/sculpture/style/ribbed/'),
    (r'^Planer\.html$', '/sculpture/style/planar/'),
    (r'^Meterial.html$', '/sculpture/material/'),
    (r'^ribbed/EarlyMace.html$', '/sculpture/early-mace'),
    (r'^list/Blade.html$', '/sculpture/blade'),
    (r'^list/Ram.html$', '/sculpture/ram'),
    (r'^list/perth_p.html$', '/sculpture/conic-madrigal'),
    (r'^list/MaceP.html$', '/sculpture/mace-perry'),
    (r'^list/DoubleKnotM.html$', '/sculpture/bouble-knot-masco'),
    (r'^list/BisectedDodec.html$', '/sculpture/bisected-dodeca'),
    (r'^list/Eclipse.html$', '/sculpture/eclipse'),
    (r'^list/D2D.html$', '/sculpture/d2d'),
    (r'^bronze/daniela.htm$', '/sculpture/daniela'),
    (r'^Puzzles/ChessSet.html$', '/puzzles/chess-set'),
    (r'^puzzles/cube-chess-set$', '/puzzles/cubic-chess-set'),
    (r'^Puzzles/Double.html$', '/puzzles/double-puzzle'),
    (r'^Puzzles/Ball.html$', '/puzzles/plexi-ball-puzzle'),
    (r'^Puzzles/Zen.html$', '/puzzles/zen-puzzle'),
    (r'^email.html$', '/bio/contact/'),
    (r'^collections.html$', '/bio/collections'),
    (r'^bypiece.html$', '/sculpture/list'),
    (r'^awards.html$', '/bio/awards'),
    (r'^aluminum/Equinox.html$', '/sculpture/equinox'),
]

for old_pattern, new_url in legacy_redirects:
    urlpatterns.append(
        re_path(old_pattern, RedirectView.as_view(url=new_url, permanent=True))
    )

