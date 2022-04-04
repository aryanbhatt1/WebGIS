from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import DepartmentContactDetailsAdminResource, ItemDescriptionResource

# Register your models here.
admin.site.register(State)
admin.site.register(District)
admin.site.register(ItemCode)
admin.site.register(Item)


class DepartmentContactDetailsAdmin(ImportExportModelAdmin):
    resource_class = DepartmentContactDetailsAdminResource

    list_display = [
        'state',
        'district',
        'ItemCode',
        'quantity',
        'departmentName',
        'contactperson',
        'contactno',
        'contactEmail'
    ]


admin.site.register(DepartmentContactDetails, DepartmentContactDetailsAdmin)


class ItemDescriptionAdmin(ImportExportModelAdmin):
    resource_class = ItemDescriptionResource

    list_display = [
        'item_desc',
        'location',
        'item_live_location_source',
        'last_updation'
    ]

admin.site.register(ItemDescription, ItemDescriptionAdmin)