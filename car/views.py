from django.views.generic import ListView, DetailView
from .models import Owner
from django.views.generic import DetailView
from .models import DriverProfile
from django.views.generic import ListView, DetailView
from .models import Car, GeolocationData, StabilityData, DriverBehaviorData



class OwnerListView(ListView):
    model = Owner
    template_name = 'owner_list.html'
    context_object_name = 'owners'

class OwnerDetailView(DetailView):
    model = Owner
    template_name = 'owner_detail.html'
    context_object_name = 'owner'
from django.views.generic import ListView, DetailView
from .models import Car, GeolocationData, StabilityData, DriverBehaviorData

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        context['geolocation_data'] = GeolocationData.objects.filter(car=car)
        context['stability_data'] = StabilityData.objects.filter(car=car)
        context['driver_behavior_data'] = DriverBehaviorData.objects.filter(car=car)
        return context

class CarListView(ListView):
    model = Car
    template_name = 'car_list.html'
    context_object_name = 'cars'

class CarDetailView(DetailView):
    model = Car
    template_name = 'car_detail.html'
    context_object_name = 'car'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        car = self.object
        context['geolocation_data'] = GeolocationData.objects.filter(car=car)
        context['stability_data'] = StabilityData.objects.filter(car=car)
        context['driver_behavior_data'] = DriverBehaviorData.objects.filter(car=car)
        return context


class DriverProfileView(DetailView):
    model = DriverProfile
    template_name = 'driver_profile.html'
    context_object_name = 'driver_profile'
