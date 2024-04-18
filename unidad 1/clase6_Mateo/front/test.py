import requests

response = requests.get("http://localhost:8000")

print (response.content)

data = {
    "marca" : "Prueba",
    "color" : "Prueba descripción",
    "tipo" : "04/04/2024",
    "material" : "Prueba"
}

response = requests.post("http://localhost:8000/v1/lapicero", data= data)

print(response.status_code)

print(response.content)