#from typing import Union
#from fastapi import FastAPI
import os
import firebase
from firebase_secrets import fireBaseConfig

firebase = firebase.initialize_app(fireBaseConfig)

db_auth = firebase.auth()
db_user = db_auth.sign_in_with_email_and_password(
  os.environ.get('FIREBASE_EMAIL'),
  os.environ.get('FIREBASE_PASSWORD')
)
db = firebase.database()
'''
app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    # return {"item_id": item_id, "q": q}
    return db.child('items').get()

'''