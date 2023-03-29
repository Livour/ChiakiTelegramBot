import secrets
import requests
from os import getenv


def get_new_pkce_verifier() -> str:
    """
    The OAuth workflow is susceptible to the authorisation code interception attack. The PKCE protocol has been designed to mitigate this threat.

    Before you can authenticate a user, your client needs to generate a Code Verifier and a Code Challenge.
    A Code Verifier is a high-entropy, cryptographic, random string containing only the characters [A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~".
    The length of the string must be between 43 and 128 characters (personally, I would recommend using 128 characters).

    MAL only allows the plain transformation for the Code Challenge. In other words, it means that you have to set the Code Challenge equal to the Code Verifier. Simple.

    :return: Newly PKCE generated token
    """
    token = secrets.token_urlsafe(100)
    return token[:128]


def mal_api_authorization():
    url = "https://myanimelist.net/v1/oauth2/authorize"
    client_id = getenv("mal_client_id")
    state = getenv("mal_state")
    try:
        response = requests.get(url,
                                params={"response_type": "code", "client_id": client_id, "state": state,
                                        "code_challenge": get_new_pkce_verifier()})
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err[0])
    return response
