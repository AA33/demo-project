__author__ = 'abhishekanurag'

from django.forms.models import formset_factory, inlineformset_factory
from django import forms
from models import Trip, Destination


class SignupForm(forms.Form):
    username = forms.CharField(max_length=30, min_length=1)
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())


class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput())


'''
class AddDestinationForm(forms.Form):
    destination_name = forms.CharField(max_length=100)
    location_lat = forms.FloatField()
    location_long = forms.FloatField()
    destination_description = forms.CharField(max_length=500)
    rating = forms.IntegerField(default=5, max_value=10, min_value=1)


DestinationFormSet = formset_factory(AddDestinationForm, can_delete=True)
'''

TripFormSet = inlineformset_factory(Trip, Destination)

'''
<input type="text" value="{{ trip.trip_name }}" name="trip_name">
    <input type="datetime" value="{{ trip.start_date }}" name="start_date"> to <input type="datetime" value="{{ trip.end_date }}" name="end_date">
    </br>
    <textarea name="trip_description">{{ trip.trip_description }}</textarea>
    <ul>
        {% for destination in trip.destination_set.all %}
            <li>
                <span>Destination: <input type="text" value="{{ destination.destination_name }}" name="destination_name_{{ forloop.counter0 }}"></span>
                <span>Rating: <input type="number" value="{{ destination.rating }}" name="rating_{{ forloop.counter0 }}"></span>
                <span>Description: <textarea name="destination_description_{{ forloop.counter0 }}">{{ destination.destination_description }}</textarea></span>
            </li>
        {% empty %}
            <li>No destinations.</li>
        {% endfor %}
        <button value="Add destination" onclick="{% include "travel_log/destination.html" %}"></button>
    </ul>
'''

'''
class AddTripForm(forms.Form):
    trip_name = forms.CharField(max_length=100)
    start_date = forms.DateTimeField()
    end_date = forms.DateTimeField()
    trip_description = forms.CharField(max_length=500)
    destination_formset = DestinationFormSet()
    '''