import os
import json
import time
import requests
import sys as n
import time as mm
from urllib.parse import quote
from get_query_id import query_id


def slow(M):
    for c in M + '\n':
        n.stdout.write(c)
        n.stdout.flush()
        mm.sleep(1. / 100)

def save_to_file(url, username,id):
    response = requests.get(url, allow_redirects=True)
    filename = id + "_" + url.split('?')[0].split('/')[-1]
    open(f'{username}/{filename}' , 'wb').write(response.content)
    return filename

query_hash=query_id(4)
variables= {
    "first":5
}
headers = {
    'User-Agent': 'My User Agent 1.0'
}
insta_uri = "https://www.instagram.com/graphql/query/"
joker = True
media = []
slow(""" 
███████╗ █████╗ ██╗   ██╗███████╗
██╔════╝██╔══██╗██║   ██║██╔════╝
███████╗███████║██║   ██║█████╗  
╚════██║██╔══██║╚██╗ ██╔╝██╔══╝  
███████║██║  ██║ ╚████╔╝ ███████╗
╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝
                   ╔═╗┌─┐┌─┐┌┬┐  
                   ╠═╝│ │└─┐ │   
                   ╩  └─┘└─┘ ┴  ██╗
         | vv1ck |              ╚═╝
__________________________________________
""")
time.sleep(1)
username = input('[!]-> Enter user : ').rstrip()
time.sleep(1)
print("\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
print(" ")
user_url = f'https://www.instagram.com/{username}/?__a=1'
resp = json.loads(requests.get(user_url, headers = headers).content.decode())
uid = resp.get('logging_page_id',-1)
if(uid == -1):
    exit()
uid = uid.split('_')[1]
variables['id'] = uid
loc = os.path.join(os.getcwd(), username)
try:  
    os.mkdir(loc)
except OSError as error:  
    pass 

while(joker):

    final_uri = f"{insta_uri}?query_hash={query_hash}&variables={quote(json.dumps(variables))}"
    print(final_uri,'----')
    resp = json.loads(requests.get(final_uri, headers = headers).content.decode())
    cont = resp['data']['user']['edge_owner_to_timeline_media']
    for i in cont['edges']:
        print("\n\n[>] Done Post",i['node']['id'])
        print("====================================")
        if(i['node']['__typename'] == 'GraphSidecar'):
            sidecar = i['node']['edge_sidecar_to_children']['edges']
        else:
            sidecar = [i]
        for i in sidecar:
            if(i['node']['__typename'] == 'GraphVideo'):
                media_link = i['node']['video_url']
            elif(i['node']['__typename'] == 'GraphImage'):
                media_link = i['node']['display_resources'][-1]['src']
            else:
                print(i['node']['__typename'],'-----------------')
                input()
            media.append(media_link)
            fname = save_to_file(media_link, username, i['node']['id'])
            print("\t[>] saved",fname)
            print("====================================")
    joker = cont['page_info']['has_next_page']
    if(joker):
        variables['after'] = cont['page_info']['end_cursor']
    input("الاستمرار ؟ Enter ")

