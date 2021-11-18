from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security import authenticate, identity
from resources.user import UserRegister
from resources.item import Item, ItemList
from datetime import timedelta
from resources.store import Store, StoreList

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = "Vicento1816!"
api = Api(app)

@app.before_first_request
def create_tables():
    db.create_all()


app.config["JWT_AUTH_URL_RULE"] = "/login"
jwt = JWT(app, authenticate, identity) #/auth

#Config JWT to expire within half an hour
app.config["JWT_EXPIRATION_DELTA"] = timedelta(seconds = 1800)

api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>") #7.0.0.1:5000/item/Michiel
api.add_resource(ItemList, "/items")
api.add_resource(StoreList, "/stores")
api.add_resource(UserRegister, "/register")

#als naam == de app applicatie, run; zo niet, dan niet runnen -> als je het bestand importeert bijv. 
if __name__ == "__main__":
    from db import db
    db.init_app(app)
    app.run(port=5000,debug=True)




