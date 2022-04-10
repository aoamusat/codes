import pandas as pd
from pypodio2 import api
from os import environ as env


client_id = env.get('PODIO_CLIENT_ID')
client_secret = env.get('PODIO_CLIENT_SECRET')
username = env.get('PODIO_USERNAME')
password = env.get('PODIO_PASSWORD')

podio = api.OAuthClient(
    		client_id,
        	client_secret,
        	username,
        	password)

task_board_app_id = 27017268
ajustes_app_id = 26033392

app_info = podio.Application.find(ajustes_app_id)
labels = []
for field in app_info.get('fields'):
    if field['status'] == "active":
        label = field['external_id']
        label = label[:40]
        labels.append(label)


num_of_items = podio.Application.get_items(app_info.get('app_id'))['total']
data = []
for step in range(0, num_of_items, 250):
	filtered_items = podio.Item.filter(app_info.get('app_id'), {"offset": step, "sort_by": "created_on", "sort_desc": False, "limit": 250})
	items = filtered_items.get('items')
	
	for item in items:
		d = []
		d.append(str(item['item_id']))
		d.append(str(item['created_on']))

		fields = [x for x in item['fields'] if f"{x['external_id'][:40]}" in labels]
		# Fazendo a comparação entre os campos existentes e os preenchidos
        # Caso o campo esteja em branco no Podio, preencher com '?'
		j = 0
		for i in range(len(labels)):
			s = ""
			if j < len(fields) and str(fields[j]['external_id'][:40]) == labels[i]:
				# De acordo com o tipo do campo há uma determinada forma de recuperar esse dado
				if fields[j]['type'] == "contact":
					# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
					# Podem haver aspas duplas inseridas no valor do campo. Substituir com aspas simples
					for elem in fields[j]['values']:
						s += elem['value']['name'].replace("\"", "'") + "|"
					s = s[:-1]
				elif fields[j]['type'] == "category":
					s += fields[j]['values'][0]['value']['text'].replace("\"", "'")
				elif fields[j]['type'] == "date" or (fields[j]['type'] == "calculation" and 'start' in \
					fields[j]['values'][0]):
					s += fields[j]['values'][0]['start']
				elif fields[j]['type'] == "money":
					s += fields[j]['values'][0]['currency'] + " " + fields[j]['values'][0]['value']
				elif fields[j]['type'] == "image":
					s += fields[j]['values'][0]['value']['link']
				elif fields[j]['type'] == "embed":
					s += fields[j]['values'][0]['embed']['url']
				elif fields[j]['type'] == "app":
					# Nesse caso o campo é multivalorado, então concatena-se com um pipe '|'
					for val in fields[j]['values']:
						s += val['value']['title'].replace("\"", "'") + "|"
					s = s[:-1]
				elif fields[j]['type'] == "number":
					s += str(int(float(fields[j]['values'][0]['value'])))
				else:
					value = str(fields[j]['values'][0]['value'])
					s += value.replace("\"", "'")
				j += 1
			d.append(s)
		data.append(d)

#data = [['Alex',10],['Bob',12],['Clarke',13]]
df = pd.DataFrame(data,columns=['item-id', 'created-on']+labels)
print (df)