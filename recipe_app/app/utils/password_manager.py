from passlib.hash import bcrypt


class PasswordManager: 
    @staticmethod
    def generate_password(init_password: str)-> str: 
        return bcrypt.hash(init_password)
    
    @staticmethod
    def verify_password(init_password: str, secret: str)->bool: 
        return bcrypt.verify(secret, init_password)

