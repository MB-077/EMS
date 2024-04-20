from django.shortcuts import render, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from .models import *


# Create your views here.
def home(request):
    try:
        if request.COOKIES["logged"] == "True":
            return HttpResponseRedirect(reverse("dashboard"))
    except KeyError:
        return render(request, "index.html")

def dashboard(request):
    context = {
        "username" : request.COOKIES["username"]
    }
    return render(request, "dashboard.html", context)

def logout(request):
    response = HttpResponseRedirect(reverse("home"))
    response.delete_cookie("logged")
    response.delete_cookie("username")
    return response

def auth_account(request):
    if request.method=="POST":
        entered_rollno = request.POST['name']
        entered_pass = request.POST['pass']

        try:
            user = User_Login.objects.get(student_roll_no=entered_rollno)
        except ObjectDoesNotExist:
            return HttpResponse("DOESNT EXIST")
        
        if user.password == entered_pass:
            response = HttpResponseRedirect(reverse("dashboard"))  # Set "username" cookie 
            response.set_cookie("username", entered_rollno)
            if not user.remember_me:
                response.session.set_expiry(0)
            else:
                response.set_cookie("logged", "True")  # Set LOGGED as TRUE iff Remember_Me = True
            return response
        else:
            # Redirect to Homepage.
            return HttpResponseRedirect(reverse("home"))