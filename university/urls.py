from django.urls import path

from . import views as university_views

urlpatterns = [
   path('' , university_views.index , name ='index'),
   path('search/' , university_views.SearchResultsView.as_view() , name ='search_result'),

   ]