import requests

url = 'http://localhost:5000/validate'
r = requests.post(url,json={'age':30, 'weight':60})
print(r.json())



url1 = 'http://localhost:5000/validates'
r1 = requests.post(url1,json={'Kilometer':56})

print(r1.json())