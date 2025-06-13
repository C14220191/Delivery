from nameko.events import EventDispatcher
from nameko.rpc import rpc
from nameko_sqlalchemy import DatabaseSession

from exceptions import NotFound  # Pastikan Anda memiliki exception ini
from models import DeclarativeBase, Delivery  # Import model Delivery
from schemas import DeliverySchema  # Import schema Delivery


class DeliveryService:
    name = 'delivery_service'

    db = DatabaseSession(DeclarativeBase)
    event_dispatcher = EventDispatcher()

    @rpc
    def get_delivery(self, delivery_id):
        delivery = self.db.query(Delivery).get(delivery_id)

        if not delivery:
            raise NotFound('Delivery with id {} not found'.format(delivery_id))

        return DeliverySchema().dump(delivery)
    
    @rpc
    def get_all_deliveries(self):
        deliveries = self.db.query(Delivery).all()
        return DeliverySchema(many=True).dump(deliveries)
    
    @rpc
    def create_delivery(self, tujuan, jarak, notes, harga_delivery, order_id, member_id):
        delivery = Delivery(
            tujuan=tujuan,
            jarak=jarak,
            notes=notes,
            harga_delivery=harga_delivery,
            order_id=order_id,
            member_id=member_id
        )
        self.db.add(delivery)
        self.db.commit()

        delivery_data = DeliverySchema().dump(delivery)

        self.event_dispatcher('delivery_created', {
            'delivery': delivery_data,
        })

        return delivery_data

    @rpc
    def update_delivery(self, delivery):
        existing_delivery = self.db.query(Delivery).get(delivery['id'])

        if not existing_delivery:
            raise NotFound('Delivery with id {} not found'.format(delivery['id']))

        existing_delivery.tujuan = delivery.get('tujuan', existing_delivery.tujuan)
        existing_delivery.jarak = delivery.get('jarak', existing_delivery.jarak)
        existing_delivery.notes = delivery.get('notes', existing_delivery.notes)
        existing_delivery.harga_delivery = delivery.get('harga_delivery', existing_delivery.harga_delivery)
        existing_delivery.order_id = delivery.get('order_id', existing_delivery.order_id)
        existing_delivery.member_id = delivery.get('member_id', existing_delivery.member_id)

        self.db.commit()
        return DeliverySchema().dump(existing_delivery)

    @rpc
    def delete_delivery(self, delivery_id):
        delivery = self.db.query(Delivery).get(delivery_id)

        if not delivery:
            raise NotFound('Delivery with id {} not found'.format(delivery_id))

        self.db.delete(delivery)
        self.db.commit()
