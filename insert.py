import requests
from datetime import datetime, timezone
ts=datetime.now(timezone.utc).isoformat()

# the URL below should be changed (can be found in Admin->Settings->System)
response=requests.get('https://admin:password@nc.example.com/ocs/v2.php/apps/serverinfo/api/v1/info?format=json')
res=response.json()['ocs']['data']
res['@timestamp']=ts

# the Elasticsearch URL (and the index name) below should also be changed 
rc=requests.post('http://localhost:9200/nextcloud-stat/_doc', json=res)
