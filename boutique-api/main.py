import json
from flask import Flask, render_template, request
from random import randint
from transaction import Transaction
import requests

app = Flask(__name__)

tran = Transaction()

# @app.route("/users",methods=['POST','GET'])
# def ff():
#     aaa = json.dumps({"id_user":12, "dhbdbg":"sfslfndflk"})
#     print(aaa)
#     return aaa

@app.route("/")
def index():
    return render_template('./index.html')

@app.route("/achat",methods=['POST'])
def achat():

    if not request and request.method != 'POST':
        return None

    nom      = request.form['nom']
    prenom   = request.form['prenom']
    date_exp = request.form['date_expiration']
    code     = request.form['code']
    cvc      = request.form['cvc']
    save     = True
    pack     = request.form['pack']

    # P2
    id_user  = ((requests.get("http://127.0.0.1:5001/users")).json())['user_id']
    id_achat = 1
    prix     = 10

    obj_cb = {
        "id_user"          : id_user,
        "nom"              : nom,
        "prenom"           : prenom,
        "date_expiration"  : date_exp,
        "code"             : code,
        "cvc"              : cvc,
        "save"             : save
    }

    obj_achat = {
        "user_id"          : id_user,
        "id_achat"         : id_achat,
        "prix"             : prix,
        "payement_accepte" : payement_is_accepted(),
        "nom_pack"         : pack

    }

    tran.insert_data_payement(obj_achat)
    tran.insert_data_cb(obj_cb)

    return json.dumps(obj_achat) if obj_achat["payement_accepte"] else "C'est non."

# 80% chance true 
def payement_is_accepted():
    random = randint(1,10)
    return random not in [1,3]

