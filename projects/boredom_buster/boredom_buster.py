import requests

response = requests.get("https://bored-api.appbrewery.com/random")

if response.status_code == 200 :
    data = response.json()
    print("Request succesfull")
    print(data["activity"])

else :
    print(f"Request error : {response.status_code} - {response.text}")

