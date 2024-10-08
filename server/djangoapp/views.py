# Uncomment the required imports before adding the code

from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404, render, redirect
from django.contrib.auth import logout
from django.contrib import messages
from datetime import datetime

from django.http import JsonResponse
from django.contrib.auth import login, authenticate
import logging
import json
from django.views.decorators.csrf import csrf_exempt
from .populate import initiate


# Get an instance of a logger
logger = logging.getLogger(__name__)


# Create your views here.

# Create a `login_request` view to handle sign in request
@csrf_exempt
def login_user(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        user = authenticate(username=username, password=password)
        response_data = {"userName": username}
        if user is not None:
            login(request, user)
            response_data['status'] = "Authenticated"
        else:
            response_data['status'] = "Authentication Failed"
        return JsonResponse(response_data)
    return JsonResponse({"error": "POST request required"}, status=405)



# Create a `logout_request` view to handle sign out request
def logout_request(request):
    if request.method == 'POST':
        # Log out the current user
        logout(request)
        
        # Return JSON response with username set to an empty string
        data = {"userName": ""}
        return JsonResponse(data)
    
    # If not a POST request, return a method not allowed error
    return JsonResponse({"error": "POST request required"}, status=405)


# Create a `registration` view to handle sign up request
@csrf_exempt
def registration(request):
    if request.method == 'POST':
        # Load JSON data from the request body
        data = json.loads(request.body)
        username = data.get('userName')
        password = data.get('password')
        first_name = data.get('firstName')
        last_name = data.get('lastName')
        email = data.get('email')

        # Check if the username already exists
        if User.objects.filter(username=username).exists():
            return JsonResponse({"error": "Already Registered"}, status=400)

        # Create the user if the username does not exist
        user = User.objects.create_user(username=username, first_name=first_name, last_name=last_name, password=password, email=email)
        user.save()

        # Log the user in
        login(request, user)

        # Return a successful registration response
        return JsonResponse({"userName": username, "status": "Authenticated"})

    return JsonResponse({"error": "Invalid request method"}, status=405)

# # Update the `get_dealerships` view to render the index page with
# a list of dealerships
# def get_dealerships(request):
# ...

# Create a `get_dealer_reviews` view to render the reviews of a dealer
# def get_dealer_reviews(request,dealer_id):
# ...

# Create a `get_dealer_details` view to render the dealer details
# def get_dealer_details(request, dealer_id):
# ...

# Create a `add_review` view to submit a review
# def add_review(request):
# ...
