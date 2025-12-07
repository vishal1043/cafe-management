import mysql.connector

class ItemDatabase():
    def __init__(self):
        self.conn = mysql.connector.connect(
                    host="localhost",
                    user="root",
                    password="0808",
                    database="cafe_management_system" 
                )
        self.cursor = self.conn.cursor()

    def get_items(self):
        result_list=[]
        query = "SELECT * FROM item"
        self.cursor.execute(query)
        result = self.cursor.fetchall()       
        for row in result:
            item_dic={}
            item_dic["id"]=row[0]
            item_dic["name"]=row[1]
            item_dic["price"]=row[2]
            result_list.append(item_dic)
        return result_list
    
    def get_item(self, item_id):
        query = f"SELECT * FROM item WHERE id='{item_id}'"
        self.cursor.execute(query)
        result = self.cursor.fetchall()
        for row in result:
            item_dic={}
            item_dic["id"]=row[0]
            item_dic["name"]=row[1]
            item_dic["price"]=row[2]
            return [item_dic]

    def add_item(self,id, body_object):
        query = f"INSERT INTO item(id,name,price) VALUES ('{id}', '{body_object['name']}', {body_object['price']})"
        self.cursor.execute(query)
        self.conn.commit()


    def update_item(self, id, body_object):
        query = f"UPDATE item SET name ='{body_object['name']}', price={body_object['price']}  WHERE id ='{id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True



    def delete_item(self, item_id):
        query = f"DELETE FROM item WHERE id='{item_id}'"
        self.cursor.execute(query)
        if self.cursor.rowcount == 0:
            return False
        else:
            self.conn.commit()
            return True
    

# db= ItemDatabase()
# db.update_item(id='e79497b4b268487bbf4edf3a79c14cdc', body_object={"name":"Mango", "price":15})
