from django.shortcuts import render
 
# Create your views here.
def cindex(request):
    import json
    import requests
    
    corona_api_request=requests.get("https://coronavirus-19-api.herokuapp.com/countries")
    api=corona_api_request.json()
    return render(request,'corona/cindex.html',{'country':api})

    