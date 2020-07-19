import jwt
import datetime
import os


class Auth():
    def getJWT(self, userName):
        payload = {
            'some': 'payload',
            'iss': 'urn:authServer',
            'iat': datetime.datetime.utcnow(),
            'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1),
            'user': userName
        }
        encoded = jwt.encode(payload, os.environ.get(
            "SECRET_KEY"), algorithm='HS256')

        return encoded

    def getPayload(self, jwtKey):
        decoded = jwt.decode(jwtKey, os.getenv(
            "SECRET_KEY"), algorithms='HS256')
        return decoded
