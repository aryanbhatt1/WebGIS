from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from .models import *
from .resources import DepartmentContactDetailsAdminResource

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
