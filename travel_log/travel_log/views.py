from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.exceptions import ObjectDoesNotExist
from django.core.urlresolvers import reverse
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, render_to_response, get_object_or_404
import dateutil.parser
from django import forms
from django.contrib.auth.models import User
from django.template import RequestContext
from travel_log.constants import *
import logging
from travel_log.forms import SignupForm, LoginForm, TripFormSet
from travel_log.models import Trip, Destination
from travel_log.utils import *

logger = logging.getLogger(__name__)


def index(request):
    return render(request, TLG_APP_NAME + '/index.html')


def userlogin(request):
    form = LoginForm()
    if request.method == HTTP_POST:
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                if user.is_active:
                    login(request, user)
                    # Redirect to a success page.
                    return HttpResponseRedirect(reverse(TLG_APP_NAME + ':home'))
                else:
                    # Return a 'disabled account' error message
                    return render(request, TLG_APP_NAME + '/login.html', {
                        TLG_ERR_MSG: "The account for the username you entered has been disabled.", 'form': form
                    })
            else:
                # Return an 'invalid login' error message.
                return render(request, TLG_APP_NAME + '/login.html', {
                    TLG_ERR_MSG: "The username or password you entered is incorrect.", 'form': form
                })
    return render(request, TLG_APP_NAME + '/login.html', {'form': form})


def signup(request):
    if request.method == HTTP_POST:
        form = SignupForm(request.POST)
        if form.is_valid():
            try:
                username = form.cleaned_data['username']
                email = form.cleaned_data['email']
                password = form.cleaned_data['password']
                user = User.objects.create_user(username, email, password)
                # todo: add specific permissions
                user.save()
                return HttpResponseRedirect(reverse(TLG_APP_NAME + ':index'))
            except IntegrityError:
                return render(request, TLG_APP_NAME + '/signup.html', {
                    TLG_ERR_MSG: "Sorry, that username has been used.",
                })
    else:
        form = SignupForm()

    return render(request, TLG_APP_NAME + '/signup.html', {'form': form})


# todo: Use @login_required(login_url=TLG_APP_NAME+'/userlogin/')
def home(request):
    if request.method == HTTP_GET:
        user = request.user
        if user.is_authenticated():
            if user.is_active:
                # Redirect to a success page.
                context = {'username': user.username, 'trips': user.trip_set.all().order_by('-start_date')}
                return render(request, TLG_APP_NAME + '/home.html', context)
            else:
                # Return a 'disabled account' error message
                return render(request, TLG_APP_NAME + '/login.html', {
                    TLG_ERR_MSG: "The account for this user has been disabled.",
                })
        else:
            # Return an 'invalid login' error message.
            form = LoginForm()
            return render(request, TLG_APP_NAME + '/login.html', {
                TLG_ERR_MSG: "Please log in first.",
                'form': form,
            })


def trip_view(request, trip_id):
    if request.method == HTTP_GET:
        trip = get_object_or_404(Trip, id=trip_id)
        show_edit = (trip.user == request.user and request.user.is_authenticated())
        context = {'trip': trip, 'show_edit': show_edit}
        return render(request, TLG_APP_NAME + '/view.html', context)


def __trip_save__(trip, request):
    trip.trip_name = request.POST.get('trip_name')
    # July 21, 2014, 12:48 a.m
    parser = dateutil.parser
    trip.start_date = parser.parse(request.POST.get('start_date'))
    trip.end_date = parser.parse(request.POST.get('end_date'))
    trip.trip_description = request.POST.get('trip_description')
    trip.save()
    dest_count = request.POST.get('dest_count')
    dest_count = dest_count[:-1].split(',')
    dest_count = map(get_int_or_neg, dest_count)
    print dest_count
    destinations = []
    for i in dest_count:
        if i >= 0:
            idx = str(i)
            dest_name = request.POST.get('destination_name_edit_' + idx)
            dest_rating = int(request.POST.get('rating_' + idx + '_edit'))
            dest_lat = float(request.POST.get('hidden_lat_' + idx))
            dest_long = float(request.POST.get('hidden_lng_' + idx))
            dest_desc = request.POST.get('destination_desc_edit_' + idx)
            dest = Destination(destination_name=dest_name, location_lat=dest_lat, location_long=dest_long,
                               destination_description=dest_desc, rating=dest_rating, trip=trip)
            destinations.append(dest)

    for prev_dest in trip.destination_set.all():
        prev_dest.delete()
    for dest in destinations:
        dest.save()


def trip_edit(request, trip_id=None):
    if not trip_id:
        trip = Trip(user=request.user)
    else:
        trip = Trip.objects.get(pk=trip_id, user=request.user)
    if request.method == HTTP_GET:
        context = {'trip': trip}
        return render(request, TLG_APP_NAME + '/edit.html', context)
    elif request.method == HTTP_POST:
        __trip_save__(trip, request)
        return HttpResponseRedirect(reverse(TLG_APP_NAME + ':home'))


def trip_delete(request, trip_id):
    print 'deleting' + trip_id
    if request.method == HTTP_GET:
        trip = Trip.objects.get(pk=trip_id).delete()
        return HttpResponseRedirect(reverse(TLG_APP_NAME + ':home'))


def userlogout(request):
    logout(request)
    return HttpResponseRedirect(reverse(TLG_APP_NAME + ':index'))

