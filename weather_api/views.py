from django.shortcuts import render
import requests

def call_api(city):
        url = "http://api.weatherapi.com/v1/current.json"
        headers = {
            
            "Accept": "application/json"
        }

        params = {
            "Key": "48dd08d8004d49b586e70018232108",
            "q": city,
            "aqi": "yes"
        }
        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            data = response.json()
            return data
      
        else:
            return None
           

def result(request):
    city = request.GET.get('city')
    data = call_api(city)
    print(data)
    if(data == None):
       
        return render(request,'error.html')
    return render(request,'result.html',data)

def api_key(request):
    return render(request,'index.html')
    
    