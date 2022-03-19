from django.shortcuts import render
from .models import AccountUser
# Create your views here.
def login(request):
    if request.method=='POST':
        AccountUser(user_name=request.POST.get('name'),user_password=request.POST.get('password')).save()
    return render(request,'account/login.html')
