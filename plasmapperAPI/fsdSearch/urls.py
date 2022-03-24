from django.urls import path
from . import views

urlpatterns = [
  path('features', views.doFsdSearch, name='fsdSearch'),
  path('plasmids', views.getPlasmidSequence, name='plasmidSequence'),
  path('plasmids/meta', views.getPlasmidMeta, name='plasmidMeta'),
  path('plasmids/popularity', views.incrementPopularity, name='incrementPopularity')
]