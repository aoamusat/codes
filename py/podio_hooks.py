from flask import Flask,request

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Webhooks with Python'

@app.route('/ajustes/item.create', methods=['POST'])
def itemCreate():
    data = request.form
    if 'code' in data:
        print('Verificação do hook iniciada. Código: %s' % data['code'])
    else:
        print('=== Item Criado ID -> %s ===' % data['item_id'])
        #item = podio.Item.find(data['item_id'])

    return data

@app.route('/ajustes/item.delete', methods=['POST'])
def itemDelete():
    data = request.form
    if 'code' in data:
        print('Verificação do hook iniciada. Código: %s' % data['code'])
    else:
        print('=== Item Excluído ID -> %s ===' % data['item_id'])
    return data


if __name__ == '__main__':
    app.run(debug=True, port=80)