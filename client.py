import requests


response = requests.post("https://localhost:8000/essay/invoke",
                         json = {'input':{'topic':"Agentic AI"}},
                         verify=False)

print(response.json()['output']['content'])