from django.urls import path
from titanic.api import views as api_views

urlpatterns = [
    path('person/', api_views.person_list_create_api_view, name='persons-list'),
    path('person/sex/<str:sex>', api_views.person_list_sex, name='person-filter-sex'),
    path('person/pk/<int:pk>', api_views.person_detail_api_view, name='person-detail'),
]