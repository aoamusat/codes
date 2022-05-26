import pandas as pd
from pypodio2 import api
import os
from dotenv import load_dotenv

load_dotenv()

client_id = os.getenv('PODIO_CLIENT_ID')
client_secret = os.getenv('PODIO_CLIENT_SECRET')
username = os.getenv('PODIO_USERNAME')
password = os.getenv('PODIO_PASSWORD')

podio = api.OAuthClient(client_id,client_secret,username,password)

task_board_app_id = 27017268
ajustes_app_id = 26033392

app_info = podio.Application.find(ajustes_app_id)
column_labels = []
for field in app_info.get('fields'):
    if field['status'] == "active":
        label = field['external_id']
        label = label[:40]
        column_labels.append(label)


num_of_items = podio.Application.get_items(app_info.get('app_id'))['total']
datatable = []
for step in range(0, num_of_items, 250):
	filtered_items = podio.Item.filter(app_info.get('app_id'), {"offset": step, "sort_by": "created_on", "sort_desc": False, "limit": 250})
	items = filtered_items.get('items')
	
	for item in items:
		row = []
		row.append(str(item['item_id']))
		row.append(str(item['created_on']))

		fields = [x for x in item['fields'] if f"{x['external_id'][:40]}" in column_labels]
		# Fazendo a comparação entre os campos existentes e os preenchidos
        # Caso o campo esteja em branco no Podio, preencher com '?'
		j = 0
		for i in range(len(column_labels)):
			col_value = ""
			if j < len(fields) and str(fields[j]['external_id'][:40]) == column_labels[i]:
				# De acordo com o tipo do campo há uma determinada forma de recuperar esse dado
				if fields[j]['type'] == "contact":
					# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
					# Podem haver aspas duplas inseridas no valor do campo. Substituir com aspas simples
					for elem in fields[j]['values']:
						col_value += elem['value']['name'].replace("\"", "'") + "|"
					col_value = col_value[:-1]
				elif fields[j]['type'] == "category":
					col_value += fields[j]['values'][0]['value']['text'].replace("\"", "'")
				elif fields[j]['type'] == "date" or (fields[j]['type'] == "calculation" and 'start' in \
					fields[j]['values'][0]):
					col_value += fields[j]['values'][0]['start']
				elif fields[j]['type'] == "money":
					col_value += fields[j]['values'][0]['currency'] + " " + fields[j]['values'][0]['value']
				elif fields[j]['type'] == "image":
					col_value += fields[j]['values'][0]['value']['link']
				elif fields[j]['type'] == "embed":
					col_value += fields[j]['values'][0]['embed']['url']
				elif fields[j]['type'] == "app":
					# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
					for val in fields[j]['values']:
						col_value += val['value']['title'].replace("\"", "'") + "|"
					col_value = col_value[:-1]
				elif fields[j]['type'] == "number":
					col_value += str(int(float(fields[j]['values'][0]['value'])))
				else:
					col_value += str(fields[j]['values'][0]['value']).replace("\"", "'")
				j += 1
			row.append(col_value)
		datatable.append(row)

#data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(datatable,columns=['item-id', 'created-on']+column_labels)
print (df)
