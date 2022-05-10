from django.urls import path
from titanic.api import views as api_views

urlpatterns = [
    path('person/', api_views.PersonListCreateAPIView.as_view(), name='persons-list'),
    path('person/pk/<int:pk>', api_views.PersonDetailAPIView.as_view(), name='person-detail'),
    path('person/sex/<str:sex>', api_views.PersonListSexAPIView.as_view(), name='person-filter-sex'),
]