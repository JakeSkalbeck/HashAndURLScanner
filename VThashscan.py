import requests

def checkHash(hash, VTapiKey): ### Checks the hash with VirusTotal
    headers={"Content-Type":"text"}
    params = {'apikey':VTapiKey, 'resource':hash}
    response = requests.post('https://www.virustotal.com/vtapi/v2/file/report', params=params, headers=headers)
    json_response = response.json()
    print('\nMD5 Hash:{}'.format(json_response.get('md5')))
    print("VT Threat Score: {}/{}".format(json_response.get('positives'),json_response.get('total')))
    print("Scanned Date: {}" .format(json_response.get('scan_date')))
    print("VT Link: {}\n".format(json_response.get('permalink')))

if __name__ == '__main__':
    pass