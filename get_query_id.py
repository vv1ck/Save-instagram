import requests
import re
def query_id(a:int = 4):
    resp = requests.get('https://www.instagram.com/static/bundles/es6/Consumer.js/b75e6b6ebcdc.js')
    consumerJS = resp.content.decode()
    pattern = re.compile('queryId:"[a-z0-9]{32}')
    queryid_list = pattern.findall(consumerJS)
    return queryid_list[a-1][9:]
