from pypodio2 import api
import os
from dotenv import load_dotenv
import json

load_dotenv()

client_id = os.getenv('PODIO_CLIENT_ID')
client_secret = os.getenv('PODIO_CLIENT_SECRET')
username = os.getenv('PODIO_USERNAME')
password = os.getenv('PODIO_PASSWORD')

try:
    podio = api.OAuthClient(
            client_id,
            client_secret,
            username,
            password
        )
except api.transport.TransportException as err:
    print(f"Erro no acesso a API. {err}")
    if err.status['status'] == '400' and json.loads(err.content)['error_detail'] == 'oauth.client.invalid_secret':
        print('Secret inválido.')
    elif err.status['status'] == '401':
        print('Token expirado.')
    exit(1)
else:
    orgs = podio.Org.get_all()
    workspaces = podio.Space.find_all_for_org(orgs[0]['org_id'])
    space = podio.Space.find(7589265)
    app = podio.Application.find(26460017)
    item = podio.Item.find(2064843308)
    filtered_items = podio.Item.filter(26107969, {"offset": 0, "sort_by": "created_on", "sort_desc": False, "limit": 30})
    print(item)

    # Streamers -> 26531983
    # Colaboradores -> 26107975
    # Metas -> 26107971
    # Calendario -> 26319140

    # while True:
    #     try:
    #         orgs = podio.Org.get_all()
    #     except api.transport.TransportException as err:
    #         if err.status['status'] == '401':
    #             print('Token expirado. Renovando... '+str(err))
    #             change_podio(podio)
    #         else:
    #             print(str(err))
    #     else:
    #         print(orgs)
    #print(podio)
