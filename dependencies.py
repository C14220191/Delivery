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
            INSERT INTO delivery (tujuan, jarak, notes, harga_delivery, order_id, member_id, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data.get("tujuan"),
            jarak,
            data.get("notes"),
            harga_delivery,
            data.get("order_id"),
            data.get("member_id"),
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
            data.get("status"),
            delivery_id
        )
        cursor.execute(sql, values)
        return {"message": "Delivery updated", "id": delivery_id}
    
    def delete_delivery(self, delivery_id):
        cursor = self.conn.cursor()
        cursor.execute("DELETE FROM delivery WHERE id = %s", (delivery_id,))
        return {"message": "Delivery deleted", "id": delivery_id}
    
    