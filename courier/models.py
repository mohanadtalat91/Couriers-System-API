from django.db import models

# CourierMan - Waybill - Shipment

# CourierMan
#   |--Waybill
#       |-----Shipment


class Shipment(models.Model):
    id_shipment = models.IntegerField()
    weight = models.IntegerField()
    number_of_items = models.IntegerField()
    status = models.CharField(max_length=10)


class Waybill(models.Model):
    id_waybill = models.IntegerField(blank=True, null=True)
    source = models.CharField(max_length=50, blank=True, null=True)
    destination = models.CharField(max_length=50, blank=True, null=True)
    receiver_name = models.CharField(max_length=50, blank=True, null=True)
    receiver_mobile = models.CharField(max_length=50, blank=True, null=True)
    address = models.CharField(max_length=50, blank=True, null=True)
    status = models.CharField(max_length=50, blank=True, null=True)

    shipment = models.OneToOneField(Shipment, on_delete=models.CASCADE, null=True)


class CourierMan(models.Model):
    id_courier = models.IntegerField(blank=True, null=True)
    first_name = models.CharField(max_length=15)
    last_name = models.CharField(max_length=15, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    username = models.CharField(max_length=20, blank=True, null=True)

    waybill = models.OneToOneField(Waybill, on_delete=models.SET_NULL, null=True)



