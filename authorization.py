import os
from stravalib import Client
from dotenv import load_dotenv
import webbrowser
import json
from datetime import datetime, timedelta

load_dotenv()
client_id = os.getenv('STRAVA_CLIENT_ID')
client_secret = os.getenv('STRAVA_CLIENT_SECRET')
redirect_url = os.getenv('REDIRECT_URL')

client = Client()

def refresh_access_token(refresh_token):
    token_response = client.refresh_access_token(
        client_id=client_id,
        client_secret=client_secret,
        refresh_token=refresh_token
    )
    return token_response

def load_tokens():
    try:
        with open('strava_tokens.json', 'r') as f:
            tokens = json.load(f)
            return tokens
    except FileNotFoundError:
        return None

def save_tokens(tokens):
    with open('strava_tokens.json', 'w') as f:
        json.dump(tokens, f)

def auth():
    tokens = load_tokens()
    if tokens:
        expires_at = tokens.get('expires_at')
        if expires_at and datetime.utcfromtimestamp(expires_at) > datetime.utcnow():
            access_token = tokens['access_token']
            refresh_token = tokens['refresh_token']
        else:
            token_response = refresh_access_token(tokens['refresh_token'])
            access_token = token_response['access_token']
            refresh_token = token_response['refresh_token']
            expires_in = token_response.get('expires_in', 21600)  # 21600 seconds = 6 hours
            token_response['expires_at'] = int((datetime.utcnow() + timedelta(seconds=expires_in)).timestamp())
            save_tokens(token_response)
    else:
        url = client.authorization_url(
            client_id=client_id,
            redirect_uri=redirect_url,
            scope=['activity:read_all']
        )
        webbrowser.open(url)

        code = input("Enter the code from the URL after authorization: ")
        token_response = client.exchange_code_for_token(
            client_id=client_id,
            client_secret=client_secret,
            code=code
        )
        access_token = token_response['access_token']
        refresh_token = token_response['refresh_token']
        expires_in = token_response.get('expires_in', 21600)  # 21600 seconds = 6 hours
        token_response['expires_at'] = int((datetime.utcnow() + timedelta(seconds=expires_in)).timestamp())
        save_tokens(token_response)

    client = Client(access_token=access_token)
    return client

