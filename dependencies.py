import mysql.connector

class Database:
    def __init__(self):
        self.conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="delivery"
        )
        self.conn.autocommit = True

    def get_all_delivery(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery")
        return cursor.fetchall()

    def get_delivery_by_id(self, delivery_id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery WHERE id = %s", (delivery_id,))
        return cursor.fetchone()
    
    def get_delivery_by_order_id(self, order_id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery WHERE order_id = %s", (order_id,))
        return cursor.fetchall()
    
    def get_delivery_by_member_id(self, member_id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery WHERE member_id = %s", (member_id,))
        return cursor.fetchall()
    
    def getDataByStatus(self, status):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery WHERE status = %s", (status,))
        return cursor.fetchall()

    def insert_delivery(self, data):
        cursor = self.conn.cursor()
        harga_per_km = 500
        jarak = data.get("jarak")
        harga_delivery = jarak * harga_per_km if jarak is not None else 0

        sql = """
            INSERT INTO delivery (tujuan, jarak, notes, harga_delivery, order_id, member_id, employee_id, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data.get("tujuan"),
            jarak,
            data.get("notes"),
            harga_delivery,
            data.get("order_id"),
            data.get("member_id"),
            data.get("employee_id", None),
            data.get("status", "pending")
        )

        cursor.execute(sql, values)
        return {"message": "Delivery created", "id": cursor.lastrowid}
    
    def get_last_delivery_data(self):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery ORDER BY id DESC LIMIT 1")
        result = cursor.fetchone()
        return result
    

    def update_status(self, delivery_id, new_status):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE delivery SET status = %s WHERE id = %s",
            (new_status, delivery_id)
        )
        return {"message": "Status updated", "id": delivery_id}
    
    def update_delivery(self, delivery_id, data):
        cursor = self.conn.cursor()
        harga_per_km = 500
        jarak = data.get("jarak")
        harga_delivery = jarak * harga_per_km if jarak is not None else 0

        sql = """
            UPDATE delivery
            SET tujuan = %s,
                jarak = %s,
                notes = %s,
                harga_delivery = %s,
                order_id = %s,
                member_id = %s,
                employee_id = %s,
                status = %s
            WHERE id = %s
        """
        values = (
            data.get("tujuan"),
            jarak,
            data.get("notes"),
            harga_delivery,
            data.get("order_id"),
            data.get("member_id"),
            data.get("employee_id", None),
            data.get("status"),
            delivery_id
        )
        cursor.execute(sql, values)
        return {"message": "Delivery updated", "id": delivery_id}
    
    def append_employee(self, delivery_id, employee_id):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE delivery SET employee_id = %s WHERE id = %s",
            (employee_id, delivery_id)
        )
        return {"message": "Employee added to delivery", "id": delivery_id}
    
    def get_delivery_by_employee_id(self, employee_id):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM delivery WHERE employee_id = %s", (employee_id,))
        return cursor.fetchall()
    
    def delete_delivery(self, delivery_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM delivery WHERE id = %s", (delivery_id,))
        return {"message": "Delivery deleted", "id": delivery_id}
    
    def search_delivery(self, query):
        cursor = self.conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM delivery WHERE tujuan LIKE %s OR CAST(member_id AS CHAR) LIKE %s OR CAST(employee_id AS CHAR) LIKE %s OR CAST(order_id AS CHAR) LIKE %s OR CAST(id AS CHAR) LIKE %s",
            ['%' + query + '%'] * 5
        )
        return cursor.fetchall()
    
