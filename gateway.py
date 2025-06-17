import eventlet
eventlet.monkey_patch()

from nameko.web.handlers import http
from nameko.rpc import RpcProxy
import json

class GatewayService:
    name = "gateway"

    delivery_rpc = RpcProxy("delivery_service")

    @http('GET', '/delivery')
    def get_all_delivery(self, request):
        try:
            data = self.delivery_rpc.fetch_all_delivery()
            return 200, json.dumps({"data": data})
        except Exception as e:
            return 500, json.dumps({"error": str(e)})
        
    @http('GET', '/delivery/<string:status>')
    def get_delivery_by_status(self, request, status):
        try:
            data = self.delivery_rpc.getDataByStatus(status)
            return 200, json.dumps({"data": data})
        except Exception as e:
            return 500, json.dumps({"error": str(e)})
    
    @http('GET', '/delivery/last')
    def get_last_delivery_data(self, request):
        try:
            data = self.delivery_rpc.get_last_delivery_data()
            if data:
                return 200, json.dumps({"data": data}, indent=4)
            else:
                return 404, json.dumps({"error": "No delivery found"})
        except Exception as e:
            return 500, json.dumps({"error": str(e)})


    @http('GET', '/delivery/<int:delivery_id>')
    def get_delivery_by_id(self, request, delivery_id):
        try:
            data = self.delivery_rpc.fetch_delivery_by_id(delivery_id)
            if data:
                return 200, json.dumps({"data": data})
            else:
                return 404, json.dumps({"error": "Delivery not found"})
        except Exception as e:
            return 500, json.dumps({"error": str(e)})

    @http('POST', '/delivery')
    def create_delivery(self, request):
        try:
            body = json.loads(request.get_data(as_text=True))
            result = self.delivery_rpc.create_delivery(body)
            return 201, json.dumps(result)
        except Exception as e:
            return 500, json.dumps({"error": str(e)})

    @http('POST', '/search')
    def search_location(self, request):
        try:
            body = json.loads(request.get_data(as_text=True))
            query = body.get('q') or body.get('query') or body.get('place')
            if not query:
                return 400, json.dumps({"error": "Query field (q) is required"})
            result = self.delivery_rpc.search_location(query)
            return 200, json.dumps(result)
        except Exception as e:
            return 500, json.dumps({"error": str(e)})

    @http('POST', '/distance')
    def get_distance(self, request):
        try:
            body = json.loads(request.get_data(as_text=True))
            lat = float(body.get('lat'))
            lon = float(body.get('lon'))
            result = self.delivery_rpc.get_distance(lat, lon)
            return 200, json.dumps(result)
        except Exception as e:
            return 400, json.dumps({"error": str(e)})

    @http('PUT', '/delivery/<int:delivery_id>/status')
    def update_status(self, request, delivery_id):
        try:
            body = json.loads(request.get_data(as_text=True))
            new_status = body.get("status")
            if not new_status:
                return 400, json.dumps({"error": "Status is required"})
            result = self.delivery_rpc.update_delivery_status(delivery_id, new_status)
            return 200, json.dumps(result)
        except Exception as e:
            return 500, json.dumps({"error": str(e)})

    @http('PUT', '/delivery/<int:delivery_id>')
    def update_delivery(self, request, delivery_id):
        try:
            body = json.loads(request.get_data(as_text=True))
            result = self.delivery_rpc.update_delivery(delivery_id, body)
            return 200, json.dumps(result)
        except Exception as e:
            return 500, json.dumps({"error": str(e)})
        
    @http('DELETE', '/delivery/<int:delivery_id>')
    def delete_delivery(self, request, delivery_id):
        try:
            result = self.delivery_rpc.delete_delivery(delivery_id)
            return 200, json.dumps(result)
        except Exception as e:
            return 500, json.dumps({"error": str(e)})
    
