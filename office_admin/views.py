from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'officetemplates/home.html')
def viewstaff(request):
    return render(request,'officetemplates/viewstaff.html')