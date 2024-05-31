from flask import Flask

app = Flask(__name__)

@app.route('/wellcome/', defaults={'name': None, 'ncontrol': None})
@app.route('/wellcome/<name>/', defaults={'ncontrol': None})
@app.route('/wellcome/<name>/<int:ncontrol>')
def bienvenido(name, ncontrol):
    if name is None and ncontrol is None:
        return 'Bienvenido'
    elif name is not None and ncontrol is None:
        return f'Bienvenido {name}'
    elif name is None and ncontrol is not None:
        return f'El número recibido es: {ncontrol}'
    else:
        return f'Bienvenido {name}. Tu número de control es: {ncontrol}'