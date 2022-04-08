from django.shortcuts import render
from .models import *
from geopy.geocoders import MapBox


# Create your views here.

def AddressToCoordinates(state_form, district_form, itemcode_form, item_form):
    address = DepartmentContactDetails.objects.values_list('departmentAddress', flat=True).filter(
        state__state=str(state_form)).filter(district__district=str(district_form)).filter(
        ItemCode__ItemCode=str(itemcode_form)).filter(Item__Item=str(item_form))
    print(address)
    final_address = []
    geolocator = MapBox(
        'pk.eyJ1IjoiYXJ5YW5iaGF0dDEwMDIiLCJhIjoiY2tqaDFmcnloNDFpYTJybnFvbmk0cTliNyJ9.ImW_FZl5b1VBm1bYaLyziA')
    for i in address:
        dic = {
            "latitude": 1.0,
            "longitude": 2.0,
            "departmentName": "ABC",
        }
        location = geolocator.geocode(str(i))
        dic["latitude"] = location.latitude
        dic["longitude"] = location.longitude
        dic["departmentName"] = list(DepartmentContactDetails.objects.values_list('departmentName', flat=True).filter(
            departmentAddress=str(i)).filter(ItemCode__ItemCode=str(itemcode_form)).filter(Item__Item=str(item_form)))[0]
        dic["departmentAddress"] = str(i)
        dic["contactperson"] = list(DepartmentContactDetails.objects.values_list('contactperson', flat=True).filter(
            departmentAddress=str(i)).filter(ItemCode__ItemCode=str(itemcode_form)).filter(Item__Item=str(item_form)))[0]
        dic["contactno"] = list(DepartmentContactDetails.objects.values_list('contactno', flat=True).filter(
            departmentAddress=str(i)).filter(ItemCode__ItemCode=str(itemcode_form)).filter(Item__Item=str(item_form)))[0]
        dic["contactEmail"] = list(DepartmentContactDetails.objects.values_list('contactEmail', flat=True).filter(
            departmentAddress=str(i)).filter(ItemCode__ItemCode=str(itemcode_form)).filter(Item__Item=str(item_form)))[0]
    return final_address


def home(request):
    final_address = None
    state = State.objects.all()
    district = District.objects.all()
    itemcode = ItemCode.objects.all()
    item = Item.objects.all()
    if request.method == "POST":
        state_form = request.POST['state']
        district_form = request.POST['dist']
        itemcode_form = request.POST['itemcode_form']
        item_form = request.POST['item_form']
        final_address = AddressToCoordinates(state_form, district_form, itemcode_form, item_form)



    context = {
        'final_address': final_address,
        'district': district,
        'state': state,
        'itemcode': itemcode,
        'item': item,
    }
    return render(request, 'pages/home.html', context=context)
