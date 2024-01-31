from django.shortcuts import render,HttpResponse
from W2.models import Present
from datetime import datetime
def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip
def index(request):
    context = {'variable':'I am here'}
    return render(request,'index.html',context)

def present(request):
    if request.method == "POST":
        Roll_No = request.POST.get('Roll_No')
        Password = request.POST.get('Password')
        ip_address = get_client_ip(request)

        # Check for duplicate ip_address
        existing_entry = Present.objects.filter(ip_address=ip_address).first()

        if existing_entry:
            # If the ip_address is duplicate, set ip_address to RED
            existing_entry.ip_address = '<span style="color: red;">' + ip_address + '</span>'
            existing_entry.save()
            Attendance = Present(Roll_No=Roll_No, Password=Password, Date=datetime.today(), ip_address=ip_address)
            Attendance.save()
        else:
            # If the ip_address is not duplicate, proceed to save the data
            Attendance = Present(Roll_No=Roll_No, Password=Password, Date=datetime.today(), ip_address="RED")
            Attendance.save()

    return render(request, 'present.html')

def Home(request):
    return render(request,'Home.html')
def contact(request):
    return render(request,'contact.html')
def Records(request):
    if request.method == "POST":
        Roll_No = request.POST.get('Roll_No')
        Password = request.POST.get('Password')

        # Validate the Roll_No and Password
        if Roll_No and Password:
            # Retrieve records for the entered Roll_No and Password
            attendance_data = Present.objects.filter(Roll_No=Roll_No, Password=Password)

            context = {
                "Roll_No": Roll_No,
                "AttendanceData": attendance_data
            }

            return render(request, 'Records.html', context)
    
    return render(request, 'Records.html')


