import requests
import json

def checkURL(URLScan, URLapikey):
    headers = {'API-Key':URLapikey,'Content-Type':'application/json'}
    data = {"url": URLScan, "visibility": "private"}
    response = requests.post('https://urlscan.io/api/v1/scan/',headers=headers, data=json.dumps(data))
    json_response = response.json()

    if response.status_code == 200:
        print('URL in Question: {}'.format(json_response.get('url')))
        print('Scan Result: {}'.format(json_response.get('result')))
    elif response.status_code == 400:
        print(json_response.get('message'))
        print(json_response.get('description'))
    else:
        print('Unsuccessful response not correct, try again.')
        print('Result from Scan: {}'.format(json_response()))

if __name__ == '__main__':
    pass