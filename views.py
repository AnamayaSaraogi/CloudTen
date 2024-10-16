from django.shortcuts import render,redirect
from .models import labtest, appointment
from .forms import faq

def labtests(request):
    msg = {}
    if request.method == "POST":
        unique_number = request.POST.get("unique number")
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone_number = request.POST.get("phone number")
        address = request.POST.get("address")
        email = request.POST.get("email")
        test = request.POST.get("test")

        rec = labtest(
            uno=unique_number,
            name=name,
            age=age,
            gender=gender,
            phone=phone_number,
            address=address,
            email=email,
            tests=test
        )

        rec.save()
        msg = {"msg": "Booking Confirmed..."}

    return render(request, "labtests.html", msg)


def delete_labtest(request):
    msg2 = ""
    
    if request.method == "POST":
        unique_number = request.POST.get("unique number")
        test = request.POST.get("test")

        try:
            # Try to retrieve the labtest record based on unique_number and test
            labtest_record = labtest.objects.get(uno=unique_number, tests=test)
            
            # Delete the record
            labtest_record.delete()
            msg2 = "Booking Cancelled Successfully."
        except labtest.DoesNotExist:
            msg2 = "Booking not found."

    return render(request, "labtest_cancel.html", {"msg2": msg2})

def my_bookings(request):
    rec={}
    if request.POST.get("uno"):
        rec=labtest.objects.filter(uno=request.POST.get("uno")).values()
        print(rec)
    return render(request,"my_bookings.html",{"rec":rec})

def home(request):
    if request.method=="POST":
        soc=faq(request.POST)
        if soc.is_valid():
            #print(soc)
            print(soc.cleaned_data)
            file1 = open("static/upload/questions.txt", "a")  # append mode
            file1.write(request.POST.get("ques")+"\n")
            file1.close()
            return redirect('/home')
        else:
            print("Invalid form")
    else:
        soc=faq()
        return render(request,"home.html",{'form':soc})

"""
def appointments(request):
    msg = {}
    if request.method == "POST":
        unique_number = request.POST.get("unique number")
        name = request.POST.get("name")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone_number = request.POST.get("phone number")
        address = request.POST.get("address")
        email = request.POST.get("email")
        

        rec = appointmentsct(
            uno=unique_number,
            name=name,
            age=age,
            gender=gender,
            phone=phone_number,
            address=address,
            email=email,
            
        )

        rec.save()
        msg = {"msg": "Booking Confirmed..."}

    return render(request, "appts.html", msg)


def delete_appointment(request):
    msg2 = ""
    
    if request.method == "POST":
        unique_number = request.POST.get("unique number")
        test = request.POST.get("test")

        try:
            # Try to retrieve the appointments record based on unique_number and test
            appointments_record = appointments.objects.get(uno=unique_number, tests=test)
            
            # Delete the record
            appointments_record.delete()
            msg2 = "Booking Cancelled Successfully."
        except appointments.DoesNotExist:
            msg2 = "Booking not found."

    return render(request, "appt_cancel.html", {"msg2": msg2})

"""

def appointments(request):
    msg = {}
    if request.method == "POST":
        unique_number = request.POST.get("unique_number")
        name = request.POST.get("patientName")
        age = request.POST.get("age")
        gender = request.POST.get("gender")
        phone_number = request.POST.get("phone")
        address = request.POST.get("address")
        appointment_time = request.POST.get("appointmentTime")
        doctor_name = request.POST.get("doctorName")

        rec = appointment(
            unique_number=unique_number,
            patient_name=name,
            age=age,
            gender=gender,
            phone_number=phone_number,
            address=address,
            appointment_time=appointment_time,
            doctor_name=doctor_name,
        )

        rec.save()
        msg = {"msg": "Booking Confirmed..."}

    return render(request, "appts.html", msg)

def delete_appointment(request):
    msg2 = ""
    
    if request.method == "POST":
        unique_number = request.POST.get("unique_number")

        try:
            # Try to retrieve the appointment record based on unique_number and appointment_name.
            appointment_record = appointment.objects.get(unique_number=unique_number)
            
            # Delete the record
            appointment_record.delete()
            msg2 = "Booking Cancelled Successfully."
        except appointment.DoesNotExist:
            msg2 = "Booking not found."

    return render(request, "appt_cancel.html", {"msg2": msg2})

