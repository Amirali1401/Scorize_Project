from django.shortcuts import render
from django.views import generic
from django.db.models import Q

from .models import University , Country ,City

# Create your views here.

def index(request):
    university = University.objects.all()
    return render(request , 'university/index.html' , context={'university':university})   #view 1


class SearchResultsView(generic.ListView):
    model = University
    template_name = 'search_results.html'
    context_object_name = 'university'

    def get_queryset(self):                                                  #view 2
        return  University.objects.filter(
            Q(name__icontains="Boston") | Q(city__icontains="NY") | Q(city__country__name_country__icontains="Boston"))



