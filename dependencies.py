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

    def insert_delivery(self, data):
        cursor = self.conn.cursor()
        sql = """
            INSERT INTO delivery (tujuan, jarak, notes, harga_delivery, order_id, member_id, status)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = (
            data.get("tujuan"),
            data.get("jarak"),
            data.get("notes"),
            data.get("harga_delivery"),
            data.get("order_id"),
            data.get("member_id"),
            data.get("status", "pending")  # default value
        )

        cursor.execute(sql, values)
        return {"message": "Delivery created", "id": cursor.lastrowid}
    
    def update_status(self, delivery_id, new_status):
        cursor = self.conn.cursor()
        cursor.execute(
            "UPDATE delivery SET status = %s WHERE id = %s",
            (new_status, delivery_id)
        )
        return {"message": "Status updated", "id": delivery_id}
    
    def update_delivery(self, delivery_id, data):
        cursor = self.conn.cursor()
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
            data.get("jarak"),
            data.get("notes"),
            data.get("harga_delivery"),
            data.get("order_id"),
            data.get("member_id"),
            data.get("status"),
            delivery_id
        )
        cursor.execute(sql, values)
        return {"message": "Delivery updated", "id": delivery_id}
