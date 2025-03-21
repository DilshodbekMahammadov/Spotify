
from django.contrib import admin
from django.urls import path, include
from main.views import *
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('qoshiqchilar', QoshiqchiModelViewSet)
router.register('albomlar', AlbomModelViewSet)
router.register('jadvallar', JadvallarModelViewSet)




schema_view = get_schema_view(
   openapi.Info(
      title="Spotify API",
      default_version='v1',
      description="Test description",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    # path('qoshiqchilar/', QoshiqchiAPIView.as_view()),
    # path('qoshiqchilar/<int:pk>/', QoshiqchiRetrieveUpdateDeleteAPIView.as_view()),
    path('swagger.<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),

]
