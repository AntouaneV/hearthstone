
from db import db_connect, execute 
from datetime import datetime

class Transaction:

    db = None

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

        print(save)

        if not save:
            return

        result = []

        query_cb = f'''
        SELECT * FROM carte_bancaire WHERE
        numero              = '{code}' 
        and cvc             = '{cvc}' 
        and date_expiration = '{date_expiration}' 
        and nom             = '{nom}' 
        and prenom          = '{prenom}'
        '''

        query = f'''
        INSERT INTO carte_bancaire 
        (id_user , numero , cvc , date_expiration , nom , prenom)
        VALUES 
        ({id_user}, '{code}', '{cvc}', '{date_expiration}', '{nom}', '{prenom}')
        '''

        # query_update = f'''
        # UPDATE transaction
        # SET id_cb = {}
        # WHERE (
        #     SELECT FROM 
        # )
        # '''

        try:
            print(query_cb)
            aaa = execute(self.db, query_cb).fetchone()
            print(aaa)
            if aaa :
                print("Carte existante")
                return result.append("Carte déjà existante")
            print("ok")
            print(query)
            self.manipulate_data(query, result, "cb_saved_success")
        except Exception:
            result.append("cb_saved_failed")

    def insert_data_payement(self,data):

        user_id     = data['user_id'    ]
        prix        = data['prix'       ]
        label_achat = data['label_achat']

        result = []

        query = f'''
        INSERT INTO transaction
        (id_user , label_achat , prix , date)
        VALUES 
        ('{user_id}', '{label_achat}', '{prix}', '{datetime.now()}' )
        '''

        try:
            self.manipulate_data(query, result, "payement_success")
        except Exception:
            result.append("payement_failed")


    def delete_cb(self,id_user):

        result = []

        query = f'''
        DELETE FROM carte_bancaire
        WHERE 
        id_user = {id_user}
        '''

        try:
            self.manipulate_data(query, result, "cb_deleted")
        except Exception:
            result.append("cb_deleted_failed")

    def manipulate_data(self, query, result, txt):
        execute(self.db, query)
        self.db.commit()
        result.append(txt)
        return result

 