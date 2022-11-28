from django.urls import path
from . import views

urlpatterns = [
    path('AllCourier', views.All_Courier),
    path('AddCourier', views.Add_Courier),
    path('Add_Waybill_To_Courier/<int:pk>', views.Add_Waybill_To_Courier),  # Create a Waybill
    path('GetCourier', views.Get_Courier),
    path('DeleteCourier', views.Delete_Courier),
    path('Get_Waybill_From_courier/<int:pk>', views.Get_Waybill_From_courier),  # Print a Waybill
    path('Cancel_Waybill/<int:pk>', views.Cancel_Waybill),
    path('Add_Shipment_To_Waybill/<int:pk>', views.Add_Shipment_To_Waybill),

]
