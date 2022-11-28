from rest_framework import serializers
from courier.models import CourierMan, Waybill, Shipment


class ShipmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shipment
        fields = ['id_shipment', 'weight', 'number_of_items', 'status']
        depth = 2


class WaybillSerializer(serializers.ModelSerializer):
    class Meta:
        model = Waybill
        fields = ['id_waybill', 'source', 'destination', 'status', 'shipment']
        depth = 2


class CourierManSerializer(serializers.ModelSerializer):
    class Meta:
        model = CourierMan
        fields = ['id', 'username', 'first_name', 'last_name', 'phone_number', 'waybill']
        depth = 2
