from MessangerApp.models import Message
from django.shortcuts import render
from MessangerApp.utils.helper import *
from django.http.response import HttpResponse, HttpResponseForbidden
from django.shortcuts import render
import base64

def home(request):
    user = Helper.checkSession(request) 
    if user == None:
        return render(request, 'index.html')
    return render(request, 'MessangerAppHome.html')

def register(request):
    if request.method=="POST":
        user = UserInfo(name=request.POST.get('name'),email=request.POST.get('email'),password=request.POST.get('password'))
        response = HttpResponse(DB.saveUser(user))
        request.session['email'] = user.email
        request.session['password'] = user.password
        return render(request, 'MessangerAppHome.html')
    return render(request, 'index.html')

def login(request):
    if request.method == "POST":
        try:
            user = DB.getUserByEmail(request.POST.get('email'))
            if user.password == request.POST.get('password'):
                request.session['email'] = user.email
                request.session['password'] = user.password
                return render(request, 'MessangerAppHome.html')
            else:
                return HttpResponseForbidden("User does not exists!!!")
        except UserInfo.DoesNotExist:
            return HttpResponseForbidden("User does not exists!!!")
    return render(request,"Error404.html")

def message(request):
    if request.method == "POST":
        try:
            user = Helper.checkSession(request) 
            if user != None:
                msg = Message(id= Message.genrateID(user), key = request.POST.get('key'),message = request.POST.get('message'))
                msg.save()
                dict={"id":"/"+msg.id}
                return render(request,"message.html",dict)
            else:
                return HttpResponseForbidden("User does not exists!!!")
        except UserInfo.DoesNotExist:
            return HttpResponseForbidden("User does not exists!!!")
    if request.method == "GET":
        msgs =   Message.objects.filter(id =  request.GET.get('id'))
        if msgs.first() != None:
            msg = msgs.first()
            key =  request.GET.get('key')
            dict={"key":msg.key}
            if key == msg.key:
                dict["msg"] = msg.message
            else:
                dict["msg"] = base64.b64encode(msg.message.encode())
            return render(request,"message.html",dict)
        dict={"msg":"Invalid message id"}
        return render(request,"message.html",dict)
    return render(request,"Error404.html")

def Logout(request):
    request.session['email'] = ""
    request.session['password'] = ""
    return render(request, 'index.html')
