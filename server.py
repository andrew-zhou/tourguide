from flask import Flask
app = Flask(__name__)

@app.route('/alias/<string:alias>', methods=['GET'])
def get_route_for_alias(alias):
    return
