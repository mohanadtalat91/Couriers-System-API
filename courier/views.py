from django.shortcuts import render
from .models import CourierMan, Waybill, Shipment
from .serlializer import CourierManSerializer, WaybillSerializer, ShipmentSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


# Create your views here.


@api_view(['GET'])
def All_Courier(request):
    courierMen = CourierMan.objects.all()
    serializerCourier = CourierManSerializer(courierMen, many=True)
    return Response(serializerCourier.data, status=status.HTTP_200_OK)


@api_view(['POST'])
def Add_Courier(request):
    serializerCourier = CourierManSerializer(data=request.data)
    if serializerCourier.is_valid(raise_exception=True):
        serializerCourier.save()
        return Response(serializerCourier.data, status=status.HTTP_201_CREATED)
    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def Get_Courier(request):
    try:
        courierMan = CourierMan.objects.get(id=request.data['id'])
    except CourierMan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    courierManSerializer = CourierManSerializer(courierMan)
    return Response(courierManSerializer.data, status=status.HTTP_200_OK)


@api_view(['DELETE'])
def Delete_Courier(request):
    try:
        courierMan = CourierMan.objects.get(id=request.data['id'])
    except CourierMan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    courierMan.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['PUT'])
def Add_Waybill_To_Courier(request, pk):
    try:
        courierMan = CourierMan.objects.get(id=pk)
    except CourierMan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    waybill = Waybill()

    waybill.id_waybill = request.data['id_waybill']
    waybill.source = request.data['source']
    waybill.destination = request.data['destination']
    waybill.status = request.data['status']
    waybill.save()

    courierMan.waybill = waybill
    courierMan.save()

    serializerCourier = CourierManSerializer(courierMan)
    return Response(serializerCourier.data, status=status.HTTP_205_RESET_CONTENT)


@api_view(['GET'])
def Get_Waybill_From_courier(request, pk):
    try:
        courierMan = CourierMan.objects.get(id=pk)
    except CourierMan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    waybill = courierMan.waybill
    waybillSerializer = WaybillSerializer(waybill)
    return Response(waybillSerializer.data, status=status.HTTP_200_OK)


@api_view(['PUT'])
def Cancel_Waybill(request, pk):
    try:
        courierMan = CourierMan.objects.get(id=pk)
    except CourierMan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    waybill = courierMan.waybill
    waybill.status = "Cancelled"
    waybill.save()

    courierMan.waybill = waybill
    courierMan.save()

    serializerCourier = CourierManSerializer(courierMan)
    return Response(serializerCourier.data, status=status.HTTP_205_RESET_CONTENT)


@api_view(['PUT'])
def Add_Shipment_To_Waybill(request, pk):
    try:
        waybill = Waybill.objects.get(id=pk)
    except CourierMan.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    shipment = Shipment()
    shipment.id_shipment = request.data['id_shipment']
    shipment.weight = request.data['weight']
    shipment.number_of_items = request.data['number_of_items']
    shipment.status = request.data['status']
    shipment.save()

    waybill.shipment = shipment
    waybill.save()

    serializerWaybill = WaybillSerializer(waybill)
    return Response(serializerWaybill.data, status=status.HTTP_200_OK)
