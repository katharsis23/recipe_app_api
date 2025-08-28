import uuid


class UUID_Manager: 

    @staticmethod
    def generate_uuid()->str:
        """Static method to generate uuid to users"""
        return str(uuid.uuid4())

