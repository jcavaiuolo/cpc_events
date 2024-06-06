import requests, json
from akamai.edgegrid import EdgeGridAuth

variables = {}

with open('creds.txt', 'r') as file:
    lines = file.readlines()

for line in lines:
    key, value = line.strip().split('=', 1)  # Split on the first '=' only
    variables[key.strip()] = value.strip()

s = requests.Session()
s.auth = EdgeGridAuth(
    client_token=variables['client_token'],
    client_secret=variables['client_secret'],
    access_token=variables['access_token']
)

host = variables['host']

## bring data from creds.txt

url = f"https://{host}/page-integrity/v1/pim-configs/16025/event-groups"

response = s.get(url)

print(response.json())

with open('output_file', 'w') as file:
    json.dump(response.json(), file, indent=4)
