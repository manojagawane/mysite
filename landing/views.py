from django.shortcuts import render
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from landing.models import Distributors,Shop
from django.core.urlresolvers import reverse_lazy

# Create your views here.

class IndexView(TemplateView):
    template_name = 'index.html'

class DistributorsListView(ListView):
    context_object_name = 'distributors'
    model = Distributors

class DistributorsDetailView(DetailView):
    context_object_name = 'distributors_detail'
    model = Distributors
    template_name = "landing/distributors_detail.html"

class DistributorsCreateView(CreateView):
    fields = ('name','address','latitude','longitude')
    model = Distributors

class DistributorsUpdateView(UpdateView):
    fields = ('name','address','latitude','longitude')
    model = Distributors

class DistributorsDeleteView(DeleteView):
    model = Distributors
    success_url = reverse_lazy("landing:list")
