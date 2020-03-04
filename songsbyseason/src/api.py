import flask
import flask_restful
import flask_jsonpify
import db

app = flask.Flask(__name__)
api = flask_restful.Api(app)

def format_response(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

class TopArtists(flask_restful.Resource):
    def get(self, date):
        return format_response(flask_jsonpify.jsonify(db.get_top_artists(date)))

class TopGenres(flask_restful.Resource):
    def get(self, date):
        return format_response(flask_jsonpify.jsonify(db.get_top_genres(date)))
        

api.add_resource(TopArtists, '/api/artists/<date>')
api.add_resource(TopGenres, '/api/genres/<date>')

if __name__ == '__main__':
     app.run(port='4193')