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
    user = User_Login.objects.get(student_roll_no=request.COOKIES.get("username"))

    if user.user_type == "Admin":
        datas = []
        n = User_Login.objects.exclude(user_type="Admin")
        print(f'\n{n}\n')
        for pk in n:
            data = {}
            data["student_name"] = Student.objects.get(pk=pk.student_roll_no).student_name
            data["student_roll_no"] = Student.objects.get(pk=pk.student_roll_no).student_roll_no
            data["student_room_no"] = Student.objects.get(pk=pk.student_roll_no).student_room_no
            data["room_light_status"] =  change_e_status(Room.objects.get(pk=pk.student_roll_no).room_light_status)
            data["student_hostel_out_time"] = Student.objects.get(pk=pk.student_roll_no).student_hostel_out_time
            data["student_hostel_status"] = change_status(Student.objects.get(pk=pk.student_roll_no).student_hostel_status)
            datas.append(data)
        return render(request, "admin.html", {"datas" : datas, "username" : request.COOKIES.get("username")})
    else:
        data = {}
        data["student_name"] = Student.objects.get(pk=user.student_roll_no).student_name
        data["student_room_no"] = Student.objects.get(pk=user.student_roll_no).student_room_no
        data["student_hostel_status"] = change_status(Student.objects.get(pk=user.student_roll_no).student_hostel_status)

        return render(request, "UserPage.html", data)
    

def logout(request):
    response = HttpResponseRedirect(reverse("home"))
    response.delete_cookie("logged")
    response.delete_cookie("username")
    return response

def auth_account(request):
    if request.method=="POST":
        entered_rollno = request.POST['name']
        entered_pass = request.POST['pass']
        rem_me = request.POST.get('rem_me', False)

        try:
            user = User_Login.objects.get(student_roll_no=entered_rollno)
        except ObjectDoesNotExist:
            return HttpResponse("DOESNT EXIST")
        
        if user.password == entered_pass:
            response = HttpResponseRedirect(reverse("dashboard"))  # Set "username" cookie 
            response.set_cookie("username", entered_rollno)
            if not rem_me:
                user.remember_me = rem_me
                request.session.set_expiry(0)
            else:
                response.set_cookie("logged", "True")  # Set LOGGED as TRUE iff Remember_Me = True
            return response
        else:
            # Redirect to Homepage.
            return HttpResponseRedirect(reverse("home"))

def change_status(hostel_status):
    if hostel_status == True:
        return "Yes"
    else :
        return "No"

def change_e_status(elec_status):
    if elec_status == True:
        return "On"
    else :
        return "Off"