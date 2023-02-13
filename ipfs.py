import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE
    json_data = json.dumps(data)
    files = {'file':json_data}
    url = 'https://gateway.pinata.cloud/ipfs/'
    project_id = "QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH"
    project_secret = 'ae3517feada4819223f6'
    response = requests.post(url, files=files, auth=(project_id, project_secret))
    p = response.json()
    cid = p['Hash']
    return cid


def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    params = (('arg', cid),)
    project_id = "QmbFMke1KXqnYyBBWxB74N4c5SBnJMVAiMNRcGu6x1AwQH"
    project_secret = 'ae3517feada4819223f6'
    response = requests.post('https://gateway.pinata.cloud/ipfs/', params=params, auth=(project_id, project_secret))
    data = json.loads(response.text)
    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data
