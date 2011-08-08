from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import redirect_to

urlpatterns = patterns('',
    (r'^$', 'sculpture.views.index'),
    (r'^sculpture/', include('sculpture.urls')),
    (r'^bio/', include('bio.urls')),
    (r'^puzzles/', include('puzzles.urls')),
    (r'^jewelry/', include('jewelry.urls')),
    (r'^chairs/', include('chairs.urls')),
    # line below is not needed if app.yaml defines a static_dir
    (r'^media/(.*)$', 'django.views.static.serve', {'document_root': settings.ROOT_PATH + '/media'}),
    )

legacy_urls = (
    ('^Bio\.html', '/bio/bio'),
    ('^bio/bio.html', '/bio/bio'),
    ('^eclipse/', 'sculpture/'), # http://www.mathaware.org/mam/03/
    ('index\.html', '/'),
    ('-Large\.gif/-DoubleKnot\.gif', '/media/sculpture/m/DoubleKnot_m.jpg'),
    ('-Large\.gif/-Continuum\.gif', '/media/sculpture/m/Continuum_m.jpg'),
    ('-Large\.gif/-Duality\.gif', '/media/sculpture/m/Duality_m.jpg'),
    ('^bylocation\.html', '/sculpture/map/'), 
    ('^sculpture/list.html', '/sculpture/list/'),
    ('^Ribbed\.html', '/sculpture/style/ribbed/'),
    ('^Planer\.html', '/sculpture/style/planar/'),
    ('^Meterial.html', '/sculpture/material/'),
    ('^ribbed/EarlyMace.html', '/sculpture/early-mace'),
    ('^list/Blade.html', '/sculpture/blade'),
    ('^list/Ram.html', '/sculpture/ram'),
    ('^list/perth_p.html', '/sculpture/conic-madrigal'),
    ('^list/MaceP.html ', '/sculpture/mace-perry'),
    ('^list/DoubleKnotM.html', '/sculpture/bouble-knot-masco'),
    ('^list/BisectedDodec.html', '/sculpture/bisected-dodeca'),
    ('^list/Eclipse.html', '/sculpture/eclipse'),
    ('^list/D2D.html', '/sculpture/d2d'),
    ('^bronze/daniela.htm', '/sculpture/daniela'),
    ('^Puzzles/ChessSet.html', 'puzzles/chess-set'),
    ('^Puzzles/ChessCube1.jpg', 'puzzles/cubic-chess-set-assembled_m.jpg'),
    ('^puzzles/cube-chess-set', 'puzzles/cubic-chess-set'),
    ('^Puzzles/Double.html', '/puzzles/double-puzzle'),
    ('^Puzzles/Ball.html', '/puzzles/plexi-ball-puzzle'),
    ('^Puzzles/Zen.html', '/puzzles/zen-puzzle'),
    ('^email.html', '/bio/contact/'),
    ('^collections.html', '/bio/collections'),
    ('^bypiece.html', '/sculpture/list'),
    ('^awards.html ', '/bio/awards'),
    ('^aluminum/Equinox.html', '/sculpture/equinox'),
    )

    # http://news.e-scribe.com/290 is useful 
for urltuple in legacy_urls:
    oldurl, newurl = urltuple
    urlpatterns += patterns('', 
        (oldurl, 'django.views.generic.simple.redirect_to', {'url': newurl}))

