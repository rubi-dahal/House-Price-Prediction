from flask import Flask, request, jsonify
import util
app = Flask(__name__)

@app.route('/get_location_names')
def get_location_namae():
    response = jsonify({
        'locations': util.get_location_name()
    })
    response.headers.add('Access-control-Allow-Origin','*')
    return response
    

if __name__ == '__main__':
    print("Starting server...")
    app.run()