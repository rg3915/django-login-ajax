from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.auth.views import logout
from myproject.core import views as v


urlpatterns = [
    # url(r'login/', v.login, name='login'),
    url(
        r'^logout/$',
        logout,
        {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'
    ),
    url(r'', include('myproject.core.urls', namespace='core')),
    url(r'^admin/', admin.site.urls),
]
