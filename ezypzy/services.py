
import json
import requests
from .models import bookingOrderTable,Address
from .serializers import bookingOrderTableSerializer,AddressSerializer,bookingGetterSerializer
from django.core.paginator import Paginator

def getBookingsOfCustomers(customerId):
    data = bookingOrderTable.objects.filter(customerId=customerId)
    serlizer = bookingGetterSerializer(data,many=True)
    json_data= serlizer.data
    print(json_data)
    responsData=[]
    for data in json_data:
            bookingId=data['bookingId']
            non_address_data=[]
            try:
                addressData= Address.objects.get(bookingId=bookingId)
                serlizerAddress= AddressSerializer(addressData)
                addressData=serlizerAddress.data
                addressData.pop('bookingId')
                non_address_data = {key: value for key, value in addressData.items() if value}
                # Process the addressData object
            except Address.DoesNotExist:
                # Handle the case when no address is found for the given bookingId
                addressData = None
                # Perform any necessary actions 
           
            responsData.append({'data':data, 'address':non_address_data})
    return responsData

def getBookings(purchaseOrderId):
    data = bookingOrderTable.objects.get(purchaseOrderId=purchaseOrderId)
    serlizer = bookingOrderTableSerializer(data)
    json_data= serlizer.data
    responsData=[]
    non_address_data=[]
    try:
                addressData= Address.objects.get(bookingId=json_data['bookingId'])
                serlizerAddress= AddressSerializer(addressData)
                addressData=serlizerAddress.data
                addressData.pop('bookingId')
                non_address_data = {key: value for key, value in addressData.items() if value}
                # Process the addressData object
    except Address.DoesNotExist:
                # Handle the case when no address is found for the given bookingId
                addressData = None
                # Perform any necessary actions 
    responsData.append({'data':json_data, 'address':non_address_data})
    return responsData



def getBookingsById(bookingId):
    data = bookingOrderTable.objects.get(bookingId=bookingId)
    serlizer = bookingOrderTableSerializer(data)
    json_data= serlizer.data
    responsData=[]
    non_address_data=[]
    try:
                addressData= Address.objects.get(bookingId=bookingId)
                serlizerAddress= AddressSerializer(addressData)
                addressData=serlizerAddress.data
                addressData.pop('bookingId')
                non_address_data = {key: value for key, value in addressData.items() if value}
                # Process the addressData object
    except Address.DoesNotExist:
                # Handle the case when no address is found for the given bookingId
                addressData = None
                # Perform any necessary actions 
    responsData.append({'data':json_data, 'address':non_address_data})
    return responsData


def getBookingsByCustmer(customerId,page):
    data = bookingOrderTable.objects.filter(customerId=customerId).order_by('-createdAt')
    total_results = data.count()

    page_size = 10  # Specify the number of items per page
     # Specify the desired page number

    paginator = Paginator(data, page_size)
    total_pages = paginator.num_pages

    if page > total_pages:
        page = total_pages

    page_data = paginator.page(page)
    serlizer = bookingOrderTableSerializer(page_data, many=True)
    json_data= serlizer.data
    responsData=[]
    response={}
    non_address_data=[]
    for booking in json_data:
        try:         
                    addressData= Address.objects.get(bookingId=booking['bookingId'])
                    serlizerAddress= AddressSerializer(addressData)
                    addressData=serlizerAddress.data
                    addressData.pop('bookingId')
                    non_address_data = {key: value for key, value in addressData.items() if value}
                    # Process the addressData object
        except Address.DoesNotExist:
                    # Handle the case when no address is found for the given bookingId
                    addressData = None
                    # Perform any necessary actions 
        responsData.append({'data':json_data, 'address':non_address_data})
    response = {
            'total_pages': total_pages,
            'total_results': total_results,
            'data': responsData
                }
    return response