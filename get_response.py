import requests

headers = dict()
headers['Authorization'] = 'Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNTg3NDk1MTU0LCJqdGkiOiI2YmM0MTA5NzQ2ZTg0ODFlYmY4YmYzOGEzM2IzOWUyNiIsInVzZXJfaWQiOjJ9.Cs9_uoTEmwmBFH5LNJuOp_FNMlKb-SvR7PERuRk1kvM'
res = requests.get('http://127.0.0.1:8000/paradigm/', headers=headers)

print(res.json())
for r in res.json():
    print(r)
