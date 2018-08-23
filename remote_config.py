import json

import requests
from google.auth.app_engine import Credentials, get_project_id
from google.auth.transport import requests as g_r


class RemoteConfigRequest:
    def __init__(self):
        credentials = Credentials(
            scopes=[
                "https://www.googleapis.com/auth/firebase.remoteconfig"
            ]
        )
        credentials.refresh(g_r.Request())

        self.request_url = "https://firebaseremoteconfig.googleapis.com/v1/projects/{}/remoteConfig".format(
            get_project_id()
        )
        self.token = 'Bearer {}'.format(credentials.token)

    def get(self):
        r = requests.get(self.request_url, headers={
            'Authorization': self.token
        })
        return r.json()

    def put(self, data):
        put_data = {
            "parameters": data
        }

        r = requests.put(self.request_url, json.dumps(put_data), headers={
            'Authorization': self.token,
            'If-Match': '*'
        })

        return r.json()
