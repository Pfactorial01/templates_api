from flask import Flask, jsonify, request, make_response
import jwt
from flask_restful import Api, Resource
from functools import wraps 
import pymongo
from werkzeug.security import generate_password_hash, check_password_hash

# Database connection
connection_url = "mongodb+srv://pfactorial:new_pass*123@cluster0.leidy8g.mongodb.net/?retryWrites=true&w=majority"
client = pymongo.MongoClient(connection_url)
database = client.get_database('API')
templates = database.templates
user_db = database.users
    
# flask app initialization
app = Flask(__name__)
api = Api(app)
app.config['SECRET_KEY'] = 'thisisthesecretkey'

# JWT token verification function
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if 'Authorization' in request.headers:
            token = request.headers['Authorization']

        if not token:
            return make_response('error : Token is missing!', 401) 

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
            current_user = user_db.find_one({"email": data['email']})
        except:
            return make_response('error : Token is Invalid!', 401) 

        return f(current_user, *args, **kwargs)
    return decorated

# User registration resource
class User(Resource):

    def post(self):
        data = request.get_json()
        if not data:
            return make_response("User details required", 401)
        hashed_password = generate_password_hash(data['password'], method='sha256')
        new_user = {'first_name':data['first_name'], 'last_name' : data['last_name'], 'email' : data['email'], 'password': hashed_password}
        user_db.insert_one(new_user)
        return 'User registration succesful'
api.add_resource(User, '/register')

# User Authentication resource
class Auth(Resource):

    def post(self):
        data = request.get_json()
        
        user = user_db.find_one({"email": data['email']})
        if check_password_hash(user['password'], data['password']):
            token = jwt.encode({'email': user['email']},app.config['SECRET_KEY'])
            return jsonify({'token':token})
        return make_response('Could not verify details', 401)


api.add_resource(Auth, '/login')

# Create Template and get_all Templates resource
class Template(Resource):
    @token_required
    def get(self, current_user):
        
        res = templates.find({})
        output = []

        for template in res:
            temp = {}
            temp['template_name'] = template['template_name']
            temp['subject'] = template['subject']
            temp['body'] = template['body']
            output.append(temp)
        return output
    
    @token_required
    def post(self, current_user):
        data = request.get_json()
        if not data:
            return make_response("User details required", 401)

        new_template = {'template_name':data['template_name'], 'subject' : data['subject'], 'body' : data['body']}
        templates.insert_one(new_template)
        return 'Template added succesfully'

api.add_resource(Template, '/template')

# CRUD Template resouce
class Single_Template(Resource):
    @token_required
    def get(self, current_user, template_name):
        res = templates.find_one({"template_name": template_name})
        if not res:
            return make_response("No template found", 401)

        temp = {}
        temp['body'] = res['body']
        temp['subject'] = res['subject']
        temp['template_name'] = res['template_name']

        return jsonify({'Template': temp})

    @token_required
    def put(self, current_user, template_name):
        data = request.get_json()
        if not data:
            return make_response("Details required", 401)

        templates.find_one_and_update({'template_name': template_name}, {'$set': {'template_name':data['template_name'], 'subject' : data['subject'], 'body' : data['body']}})
        return jsonify({'message': 'template updated succesfully'})

    @token_required
    def delete(self, current_user, template_name):

        res = templates.find_one({"template_name": template_name})
        if not res:
            return make_response("No template found", 401)
        
        templates.delete_one({'template_name': template_name})
        return jsonify({'message': 'template deeleted succesfully'})


api.add_resource(Single_Template, '/template/<string:template_name>')


if __name__ == '__main__':
    app.run(debug=True)

