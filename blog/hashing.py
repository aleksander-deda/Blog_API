from passlib.context import CryptContext

pwd_cxt = CryptContext(schemes=["bcrypt"], deprecated="auto")     # making the password hashed

class Hash():
    def bcrypt(password: str):
        return pwd_cxt.hash(password)
