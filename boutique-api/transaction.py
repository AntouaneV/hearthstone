
import json
from db import db_connect, execute 
from datetime import datetime
from random import randint

class Transaction:

    db     = None
    result = []

    def __init__(self):

        # Connexion à la BDD
        try:
            self.db = db_connect()
            print("Connexion réussie")
        except Exception:
            print("Echec de la connexion de la base de données")

    def insert_data_cb(self,data):
        
        id_user         = data['id_user'        ]
        nom             = data['nom'            ]
        prenom          = data['prenom'         ]
        code            = data['code'           ]
        cvc             = data['cvc'            ]
        date_expiration = data['date_expiration']
        save            = data['save'           ]

        if not save:
            return None

        query_cb = f'''
        SELECT * FROM carte_bancaire WHERE
        id_user             = '{id_user}'
        and numero          = '{code}'
        and cvc             = '{cvc}'
        and date_expiration = '{date_expiration}'
        and nom             = '{nom}' 
        and prenom          = '{prenom}'
        '''

        query = f'''
        INSERT INTO carte_bancaire 
        (id_user , numero , cvc , date_expiration , nom , prenom)
        VALUES 
        ('{id_user}', '{code}', '{cvc}', '{date_expiration}', '{nom}', '{prenom}')
        '''

        is_existant = execute(self.db, query_cb).fetchone()
        if is_existant == ():
            return self.result.append("Carte déjà existante")

        try:
            self.manipulate_data(query, self.result, "cb_saved_success")
        except Exception:
            self.result.append("cb_saved_failed")

    def insert_data_payement(self,data):

        user_id     = data['user_id'    ]
        prix        = data['prix'       ]
        nom_pack    = data['nom_pack'   ]

        query = f'''
        INSERT INTO transaction
        (id_user , label_achat , prix , date)
        VALUES 
        ('{user_id}', '{nom_pack}', '{prix}', '{datetime.now()}')
        '''

        try:
            self.manipulate_data(query, self.result, "payement_success")
            return self.add_random_cards(nom_pack)
        except Exception:
            self.result.append("payement_failed")

    def delete_cb(self,id_user):

        query = f'''
        DELETE FROM carte_bancaire
        WHERE 
        id_user = {id_user}
        '''

        try:
            self.manipulate_data(query, self.result, "cb_deleted")
        except Exception:
            self.result.append("cb_deleted_failed")

    def add_random_cards(self, nom_pack):

        match nom_pack:
            case "pack_commun":
                list_card = [randint(1,15) for _ in range(1,6)]
            case "pack_rare":
                list_card = [randint(1,20) for _ in range(1,6)]
            case "pack_epique":
                list_card = [randint(1,25) for _ in range(1,6)]

        return json.dumps({"nom_pack":nom_pack, "cards":list_card})
        

    def manipulate_data(self, query, result, txt):
        execute(self.db, query)
        self.db.commit()
        result.append(txt)
        return result