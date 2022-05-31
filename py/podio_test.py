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
    print('Access Token: '+podio.transport._headers_factory.base_headers_factory.token.access_token)
    print('Refresh Token: '+podio.transport._headers_factory.base_headers_factory.token.refresh_token)
    orgs = podio.Org.get_all()
    workspaces = podio.Space.find_all_for_org(orgs[0]['org_id'])
    app = podio.Application.find(26460017)
    item = podio.Item.find(2104343273)
    filtered_items = podio.Item.filter(26107969, {"offset": 0, "sort_by": "created_on", "sort_desc": False, "limit": 30})
    #print(item)
    task_board_appID = 27017268
    # POST 
    # Sprint -> sprint-2
    # Product Backlog -> sprint
    demandas_product_backlog_itemID = 1989362480
    sc_venda_direta_appID = 27337872
    hugo_teste_nf_appID = 26869160
    #print(podio.Item.create(task_board_appID, {'fields': {'titulo-2': ['Criar nova migração para a Cloud'],
    #                'observacoes': ['Teste'], 'difficulty': ['Average'],'sprint': [demandas_product_backlog_itemID]}}))
    #payload = {"fields":{"atendente":["teste 77"],"data-da-boleta":["2022-05-20 00:00:00"],"numero-do-pedido":["234234"],"numero-da-nf":["23423"],"valor-r-2":["234"],"forma-de-pagamento":["Cartão de Crédito - Demais bandeiras"],"parcelas":["7"],"outra-forma-de-pagamento":["Sim"],"valor-3":["8"]}}
    #print(payload)
    #print(podio.Item.create(sc_venda_direta_appID, payload))
    payload = {'fields': {'texto-2': ['Graco Teste']}}
    created_item = podio.Item.create(hugo_teste_nf_appID, payload)
    print('Created item: %s' % created_item)
    # Upload a file
    filepath = '/home/graco.silva/Downloads/okb9.xlsx'
    upload_file = podio.Files.create('okb9.xlsx', filepath)
    print('Created file: %s' % upload_file)
    # Attach the created file
    attached_file = podio.Files.attach(upload_file['file_id'], 'item', created_item['item_id'])
    print('Attached file: %s' % attached_file)
