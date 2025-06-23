import eventlet
eventlet.monkey_patch()
import requests
from nameko.rpc import rpc
from dependencies import Database

ORS_API_KEY = "5b3ce3597851110001cf62485a0dda54bf0c42858ddaa3037a8ca880"  # Ganti dengan API key kamu
GEOCODE_URL = "https://api.openrouteservice.org/geocode/search"
DIRECTION_URL = "https://api.openrouteservice.org/v2/directions/driving-car"
START_LAT = -7.339445712519114
START_LON = 112.73843681535705

class DeliveryService:
    name = "delivery_service"

    database = Database()

    @rpc
    def get_delivery_by_order_id(self, order_id):
        return self.database.get_delivery_by_order_id(order_id)
    
    @rpc
    def get_delivery_by_member_id(self, member_id):
        return self.database.get_delivery_by_member_id(member_id)
    
    @rpc
    def search_delivery(self, query):
        return self.database.search_delivery(query)
    
    @rpc
    def append_employee(self, delivery_id, employee_id):
        return self.database.append_employee(delivery_id, employee_id)
    
    @rpc
    def fetch_all_delivery_by_employee_id(self, employee_id):
        return self.database.get_delivery_by_employee_id(employee_id)

    @rpc
    def fetch_all_delivery(self):
        return self.database.get_all_delivery()

    @rpc
    def fetch_delivery_by_id(self, delivery_id):
        return self.database.get_delivery_by_id(delivery_id)

    @rpc
    def create_delivery(self, data):
        return self.database.insert_delivery(data)
    
    @rpc
    def getDataByStatus(self, status):
        return self.database.getDataByStatus(status)
    
    @rpc
    def delete_delivery(self, delivery_id):
        return self.database.delete_delivery(delivery_id)
    
    @rpc
    def get_last_delivery_data(self):
        return self.database.get_last_delivery_data()

    @rpc
    def search_location(self, query):
        try:
            response = requests.get(GEOCODE_URL, params={
                'api_key': ORS_API_KEY,
                'text': query,
                'boundary.country': 'ID',
                'size': 5
            })
            data = response.json()

            if not data["features"]:
                return {"error": "Location not found"}

            results = []
            for feature in data["features"]:
                coords = feature["geometry"]["coordinates"]
                results.append({
                    "name": feature["properties"].get("name"),
                    "label": feature["properties"].get("label"),
                    "latitude": coords[1],
                    "longitude": coords[0]
                })

            return results
        except Exception as e:
            return {"error": str(e)}


    @rpc
    def get_distance(self, dest_lat, dest_lon):
        try:
            headers = {"Authorization": ORS_API_KEY}
            json_data = {
                "coordinates": [
                    [START_LON, START_LAT],
                    [dest_lon, dest_lat]
                ]
            }
            response = requests.post(DIRECTION_URL, json=json_data, headers=headers)
            data = response.json()

            if "routes" not in data:
                return {"error": "Route not found"}

            summary = data["routes"][0]["summary"]
            return {
                "distance_km": round(summary["distance"] / 1000, 2),
                "duration_min": round(summary["duration"] / 60, 2)
            }
        except Exception as e:
            return {"error": str(e)}

    @rpc
    def update_delivery_status(self, delivery_id, status):
        return self.database.update_status(delivery_id, status)

    @rpc
    def update_delivery(self, delivery_id, data):
        return self.database.update_delivery(delivery_id, data)
