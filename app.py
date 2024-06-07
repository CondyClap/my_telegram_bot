from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/endpoint', methods=['GET'])
def handle_request():
    message = request.args.get('message')
    response = process_message(message)
    return jsonify({'reply': response})

def process_message(message):
    if message == 'informacion_del_boton':
        api_response = "Información recibida y procesada en el servidor Python."
    else:
        api_response = "Procesado: " + message
    return api_response

if __name__ == '__main__':
    # Make sure the app is running on port 8080
    app.run(host='0.0.0.0', port=8080)
