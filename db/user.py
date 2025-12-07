import mysql.connector

class UserDatabase():
    def __init__(self):
        self.conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="0808",
                    database="cafe_management_system" 
                )
        self.cursor = self.conn.cursor()

    def get_user(self, id):
        query = f"SELECT * FROM users WHERE id='{id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            user_dict = {}
            user_dict["id"] , user_dict["sername"], user_dict["password"] = row
            return user_dict
    

    def add_user(self, username, password):
        query = f"INSERT INTO users(username, password) VALUES('{username}','{password}')"
        try:
            self.cursor.execute(query)
            self.conn.commit()
            return True
        except mysql.connector.errors.IntegrityError:
            return False


    def delete_user(self, id):
        query = f"DELETE FROM users WHERE id='{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True

    def verify_user(self, username, password):
        query= f"SELECT id FROM users WHERE username='{username}'AND password='{password}'"
        self.cursor.execute(query)
        result = self.cursor.fetchone()
        if result is not None:
            return result[0]
           

