import secrets


def get_new_code_verifier() -> str:
    """
    The OAuth workflow is susceptible to the authorisation code interception attack. The PKCE protocol has been designed to mitigate this threat.

Before you can authenticate a user, your client needs to generate a Code Verifier and a Code Challenge.
 A Code Verifier is a high-entropy, cryptographic, random string containing only the characters [A-Z] / [a-z] / [0-9] / "-" / "." / "_" / "~".
 The length of the string must be between 43 and 128 characters (personally, I would recommend using 128 characters).

MAL only allows the plain transformation for the Code Challenge. In other words, it means that you have to set the Code Challenge equal to the Code Verifier. Simple.

    :return: newly PKCE generated token
    """
    token = secrets.token_urlsafe(100)
    return token[:128]


code_verifier = code_challenge = get_new_code_verifier()
