# als eerste bemerking zou ik eerder de naam van je project
# gebruik noemen, en je app aanmelden. 

from django.shortcuts import render
from django.http import JsonResponse , HttpResponse
import json
from .models import users
from django.views.decorators.csrf import csrf_exempt
from django.forms.models import model_to_dict

# Create your views here.

def getAll(request):
    # Heb je hier meteen al alle info nodig? 
    # je verstuurd hier zomaar alle paswoorden naar 1 client. 
    data = users.objects.all().values("login","password","email","role","isSuperuser")
    return JsonResponse(list(data),safe=False)

@csrf_exempt
def addUser(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    newUser = users()
    # newUser.id = post_data["id"]
    newUser.login = post_data["login"]
    newUser.password = post_data["password"]
    newUser.email = post_data["email"]
    # maak gebruik van default values - dan kan je die load verminderen
    newUser.role = post_data["role"]
    newUser.isSuperuser = post_data["isSuperuser"]
    newUser.save()
    return JsonResponse(model_to_dict(newUser),safe=False)

@csrf_exempt
def delUser(request,id):
    delUser = users.objects.get(pk = id)
    delUser.delete()
    return JsonResponse("status: gelukt",safe=False)

@csrf_exempt
def updateUser(request,id):
    # Hier moet je telkens ALLE informatie mee geven
    # is er geen mogelijkheid om dit in te korten (lijkt mij gebruiksvriendelijker)
    post_data =  json.loads(request.body.decode('utf-8'))
    updateUser = users.objects.get(pk = id)
    updateUser.login = post_data["login"]
    updateUser.password = post_data["password"]
    updateUser.email = post_data["email"]
    updateUser.role = post_data["role"]
    updateUser.isSuperuser = post_data["isSuperuser"]
    updateUser.save()
    return JsonResponse(model_to_dict(updateUser),safe=False)

@csrf_exempt
def checkUser(request):
    post_data =  json.loads(request.body.decode('utf-8'))
    # and operator werkt hier niet, het is ',' gescheiden
    queryModelObject= users.objects.get(users.login == post_data["login"] and users.password == post_data["password"] )
    
    return JsonResponse(f"data : ok info:{model_to_dict(queryModelObject)}", safe=False)


@csrf_exempt
def changePSW(request,id):
    post_data =  json.loads(request.body.decode('utf-8'))
    updateUser = users.objects.get(pk = id)
    updateUser.password = post_data["password"]
    updateUser.save()
    return JsonResponse(model_to_dict(updateUser),safe=False)
