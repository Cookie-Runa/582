import requests
import json

def pin_to_ipfs(data):
	assert isinstance(data,dict), f"Error pin_to_ipfs expects a dictionary"
	#YOUR CODE HERE
	json_data = json.dumps(data)
  files = {'file':json_data}
	  url = 'https://gateway.pinata.cloud/ipfs/QmRrDHZCj1jkmdY1kiwUod6R9cZqwViCGq1n2jkmQ2W4j9'
    project_id = "ae3517feada4819223f6"
    project_secret = '4c15fec94e9a620015a96dca3b3d525b3f49765629e949c9cb6e4ef9fdcfbee1'
    response = requests.post(url, files=files, auth=(project_id, project_secret))
    p = response.json()
    cid = p['Hash']
    return cid


def get_from_ipfs(cid,content_type="json"):
	assert isinstance(cid,str), f"get_from_ipfs accepts a cid in the form of a string"
	  params = (('arg', cid),)
    project_id = "ae3517feada4819223f6"
    project_secret = '4c15fec94e9a620015a96dca3b3d525b3f49765629e949c9cb6e4ef9fdcfbee1'
    response = requests.post('https://ipfs.infura.io:5001/api/v0/cat', params=params, auth=(project_id, project_secret))
    data = json.loads(response.text)
    assert isinstance(data, dict), f"get_from_ipfs should return a dict"
    return data