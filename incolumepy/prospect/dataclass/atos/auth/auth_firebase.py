from pathlib import Path
import firebase_admin
from firebase_admin import credentials, firestore

__author__ = "@britodfbr"  # pragma: no cover
# Auth Firebase

service_account_key = (
    Path("~")
    .expanduser()
    .joinpath(
        "projetos",
        "authkeys",
        "incolumepy-firebase-prospect-firebase-adminsdk-c4mar-ea5393e416.json",
    )
)

cred = credentials.Certificate(service_account_key)
firebase_admin.initialize_app(cred)

db = firestore.client()
