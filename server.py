from flask import Flask
app = Flask(__name__)

@app.route('/alias/<string:query>', methods=['GET'])
def get_route_for_alias(query):
    return
