import requests
import json

def pin_to_ipfs(data):
    assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
    #YOUR CODE HERE
    data_str = json.dumps(data)
    project_id = '2LgtEEG00T4DgyqA1r0k1Q28nUh'
    secret = '9b6f892c865160dfcfc002913a6838ef'
    response = requests.post('https://ipfs.infura.io:5001/api/v0/add',
                             files={'file' : data_str},auth=(project_id, secret))
    return_value = response.text
    cid = json.loads(return_value)['Hash']
    return cid

def get_from_ipfs(cid,content_type="json"):
    assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
    #YOUR CODE HERE
    url = 'https://ipfs.infura.io:5001/api/v0/cat?arg=' + cid
    params = (('arg',cid),)
    project_id = '2LgtEEG00T4DgyqA1r0k1Q28nUh'
    secret = '9b6f892c865160dfcfc002913a6838ef'
    response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=(project_id, secret))
    data = json.loads(response.text)
    assert isinstance(data,dict), f"get_from_ipfs should return a dict"
    return data


