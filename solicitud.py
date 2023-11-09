import requests 

data = { 'uname': 'admin@bank.a####', 'bank': 'abc', 'password': 'eduardo', 'btn': 'Register+me!' }
response=requests.post('http://10.10.82.187/register.php',data=data)
print(response.text)
