# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic

from .models import Property
from .forms import LookupForm
from .forms import DistanceForm

# Show the all the properties in the db.

class PropertyListView(generic.ListView):
    model = Property
    template_name = "properties/list.html"


class PropertyDetailView(generic.DetailView):
    model = Property
    template_name = "properties/detail.html"


class PropertyCreateView(generic.CreateView):
    model = Property  # what type of object we are creating?
    template_name = "properties/create.html"  # the page to display the form.
    fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
    success_url = reverse_lazy('properties:list')


class PropertyUpdateView(generic.UpdateView):
    model = Property  # what type of object we are editing?
    template_name = "properties/edit.html"  # the page to display the form.
    fields = ['prop_type', 'address', 'zip_code', 'description', 'picture_url', 'price',]
    success_url = reverse_lazy('properties:list')


class SearchFormView(generic.FormView):
    model = Property
    form_class = LookupForm
    template_name = "properties/search.html"


    def get_context_data(self, **kwargs):
        context = super(SearchFormView, self).get_context_data(**kwags)
        try:
            results = []
            q = self.request.GET['query']
            for i in Property.object.all:
                if q in i.prop_type:
                    results.append[i]

            context['result'] = results
        except:
            pass

        return context

class PropertyDistanceSearch(generic.FormView):
    model = Property
    form_class = LookupForm
    template_name = "properties/distance.html"

    def get_context_data(self, **kwargs):
        context = super(PropertyDistanceSearch, self).get_context_data(**kwags)
        try:
            result = []
            q = self.request.GET['location']
            dist = self.request.GET['distance']
            geolocator = Nominatim()
            loc = geolocator.geocode(q)


            if not loc:
                context['result'] = 'Location not found in Nominatim'
            else:
                for i in Property.object.all:
                    dloc = geolocator.geocode(i.address)
                    d = distance((loc.latitude, loc.longitude), (dloc.latitude, dloc.longitude)).miles
                    if d < dist:
                        result.append[i]
                        
                context['result'] = result
        except:
            pass

        return context