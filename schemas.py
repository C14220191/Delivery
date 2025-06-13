from marshmallow import Schema, fields


class DeliverySchema(Schema):
    id = fields.Int(required=True)
    tujuan = fields.Str(required=True)
    jarak = fields.Int(required=True)
    notes = fields.Str()
    harga_delivery = fields.Decimal(as_string=True, required=True)
    order_id = fields.Int(required=True)
    member_id = fields.Int(required=True)
