import pandas as pd
from pypodio2 import api
import os
from dotenv import load_dotenv

def get_podio_field_values(field):
	value = ''
	if field['type'] == "contact":
		# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
		# Podem haver aspas duplas inseridas no valor do campo. Substituir com aspas simples
		for elem in field['values']:
			value += elem['value']['name'].replace("\"", "'") + "|"
		value = value[:-1]
	elif field['type'] == "category":
		value += field['values'][0]['value']['text'].replace("\"", "'")
	elif field['type'] == "date" and 'start' in field['values'][0]:
		value += field['values'][0]['start']
	elif field['type'] == "money":
		value += field['values'][0]['currency'] + " " + field['values'][0]['value']
	elif field['type'] == "image":
		value += field['values'][0]['value']['link']
	elif field['type'] == "embed":
		value += field['values'][0]['embed']['url']
	elif field['type'] == "app":
		# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
		for val in field['values']:
			value += val['value']['title'].replace("\"", "'") + "|"
		value = value[:-1]
	elif field['type'] == "number":
		value += str(int(float(field['values'][0]['value'])))
	else:
		value += str(field['values'][0]['value']).replace("\"", "'")

	return value


load_dotenv()

client_id = os.getenv('PODIO_CLIENT_ID')
client_secret = os.getenv('PODIO_CLIENT_SECRET')
username = os.getenv('PODIO_USERNAME')
password = os.getenv('PODIO_PASSWORD')

podio = api.OAuthClient(client_id,client_secret,username,password)

task_board_appID = 27017268
ajustes_appID = 26033392

app_info = podio.Application.find(task_board_appID)
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
		item_iter = 0
		for app_iter in range(len(column_labels)):
			col_value = ""
			if item_iter < len(fields) and str(fields[item_iter]['external_id'][:40]) == column_labels[app_iter]:
				# De acordo com o tipo do campo há uma determinada forma de recuperar esse dado
				col_value = get_podio_field_values(fields[item_iter])
				item_iter += 1
			row.append(col_value)
		datatable.append(row)

#data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(datatable,columns=['item-id', 'created-on']+column_labels)
print (df)
