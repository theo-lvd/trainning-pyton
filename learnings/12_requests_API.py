import requests

response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

if response.status_code == 200 :
    data = response.json() 
    print("Request succesfull")
    print(data["title"])
    
else :
    print(f"Request error : {response.status_code} - {response.text}") #What and why : Error code & Terminal response

