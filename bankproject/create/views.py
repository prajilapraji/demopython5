from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import *
from django.shortcuts import get_object_or_404
# If using the reverse() function


# Create your views here.
def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('first_page')
        else:
            messages.info(request,"invalid account")
            return redirect('login')

    return render(request,"login.html")
def register(request):
    if request.method=='POST':
        username=request.POST['username']
        password = request.POST['password']
        cpassword = request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
                return redirect('register')
            else:
                user=User.objects.create_user(username=username,password=password)

                user.save();
                return redirect('login')

        else:
            messages.info(request,"password not matched")
            return redirect('register')
        return redirect('/')
    return render(request,"register.html")
def logout(request):
    auth.logout(request)
    return redirect('/')

def first_page(request):
    districts = District.objects.all()
    if request.method == "POST":
        name = request.POST.get('name')
        dob=request.POST.get('dob')
        age=request.POST.get('age')
        gender=request.POST.get('gender')
        phone=request.POST.get('phone')
        mail = request.POST.get('mail')
        address=request.POST.get('address')
        district_id = request.POST.get('district')
        branch_id = request.POST.get('branch')
        accountType=request.POST.get('accountType')
        materials = request.POST.getlist('materials')



        district_instance = get_object_or_404(District, id=district_id)
        branch_instance = get_object_or_404(Branch, id=branch_id)

        person = Person(name=name, dob=dob, age=age, gender=gender, phone=phone, mail=mail, address=address, district=district_instance,
                        branch=branch_instance, accountType=accountType, materials=materials)
        person.save()

        person.materials = ",".join(materials)
        person.save()

        messages.info(request, "APPLICATION ACCEPTED")
        return redirect('first_page')



    return render(request,"first_page.html", locals())


def get_states(request):
    district_id = request.GET['district_id']
    get_district = District.objects.get(id=district_id)
    branch = Branch.objects.filter(district=get_district)
    return render(request, 'get-states.html', locals())