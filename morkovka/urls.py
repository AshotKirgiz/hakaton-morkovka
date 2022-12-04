from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from morkovka import views, settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.home, name = "home"),
    path('accounts/', include('accounts.urls')),
]

urlpatterns += [
    path('', RedirectView.as_view(url='/home/',
permanent = True)),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
                      path('__debug__/', include(debug_toolbar.urls)),
                  ] + urlpatterns

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)