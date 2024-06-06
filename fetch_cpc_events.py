import requests, json
from akamai.edgegrid import EdgeGridAuth

def linkmod():
    
    # this function modifies the eventGroupId: It iterates through each eventGroup in the eventGroups list and updates the eventGroupId field by prefixing it with the specified URL to make it a link to the Akamai Control Center console.
    with open('output_file', 'r') as file:
        data = json.load(file)

    prefix = "https://control.akamai.com/apps/securitycenter/#/page-integrity-console?incidentId="
    for eventGroup in data.get('eventGroups', []):
        eventGroup['eventGroupId'] = prefix + eventGroup['eventGroupId']

    with open('output_file', 'w') as file:
        json.dump(data, file, indent=4)

variables = {}

## bring data from creds.txt

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

url = f"https://{host}/page-integrity/v1/pim-configs/16025/event-groups"

response = s.get(url)

# print(response.json())

with open('output_file', 'w') as file:
    json.dump(response.json(), file, indent=4)

## modify eventGroupId field to be a link to the Akamai Control Center console
linkmod()

print('Done')