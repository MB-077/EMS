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

from django.db.models import F
from django.db.models import Count


def dashboard(request):
    user = User_Login.objects.get(student_roll_no=request.COOKIES.get("username"))

    if user.user_type == "Admin":
        # Count total present students
        total_present = Student.objects.filter(student_hostel_status=True).count()

        # Count total absent students
        total_absent = Student.objects.filter(student_hostel_status=False).count()

        # Fetching all students with their corresponding rooms
        students_with_rooms = Student.objects.select_related().all()

        # Constructing data for rendering
        datas = []
        for student in students_with_rooms:
            data = {
                "student_name": student.student_name,
                "student_roll_no": student.student_roll_no,
                "student_room_no": student.student_room_no,
                "student_hostel_out_time": student.student_hostel_out_time,
                "student_hostel_status": change_status(student.student_hostel_status),
                "room_light_status": no_students_present_in_room(student.student_room_no)
            }
            datas.append(data)

        return render(request, "admin.html", {"datas": datas, "username": request.COOKIES.get("username"),
                                              "total_present": total_present, "total_absent": total_absent,
                                              "active_now": total_present})
    else:
        data = {
            "student_name": Student.objects.get(student_roll_no=user.student_roll_no).student_name,
            "student_room_no": Student.objects.get(student_roll_no=user.student_roll_no).student_room_no,
            "student_hostel_status": change_status(Student.objects.get(student_roll_no=user.student_roll_no).student_hostel_status)
        }

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
        return "Inside Hostel"
    else :
        return "Outside Hostel"
    
def no_students_present_in_room(room_number):
    # Get the room object
    number_of_students = Student.objects.filter(student_room_no=room_number)
    if number_of_students.filter(student_hostel_status=True).count() == 0:
        return "Off"
    else:
        return "On"