import requests

data=requests.get("http://127.0.0.1:8000/car/list/")
print(data.json())
print(data.status_code)