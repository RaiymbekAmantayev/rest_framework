from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from quickstart import views
from django.conf import settings
from django.conf.urls.static import static

router = routers.DefaultRouter()
router.register(r'categories', views.CategoryViewSet)
router.register(r'products', views.ProductViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('admin/', admin.site.urls),
    # path('images/<path>', views.image, name='image')
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
