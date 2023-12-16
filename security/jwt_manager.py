from fastapi import HTTPException
from jwt import encode, decode

def create_token(data: dict) -> str:
    return encode(payload=data, key='7xGPxKEZLSx8s^J9cWdADsgde#8dbb%TPBRGY6@fLa5aDbnLhDhcPj@M@R@S', algorithm='HS256')

def token_validation(token: str) -> dict:
    try:
        data: dict = decode(jwt=token, key='7xGPxKEZLSx8s^J9cWdADsgde#8dbb%TPBRGY6@fLa5aDbnLhDhcPj@M@R@S', algorithms=['HS256'])
    except:
        raise HTTPException(status_code=401, detail="Unauthorized")
    
        
    
    return data