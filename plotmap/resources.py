from import_export import fields, widgets, resources
from .models import *


class DepartmentContactDetailsAdminResource(resources.ModelResource):
    id = fields.Field(saves_null_values=False, column_name='id', attribute='id',
                      widget=widgets.IntegerWidget())
    state = fields.Field(saves_null_values=True, column_name='state',
                         attribute='state', widget=widgets.ForeignKeyWidget(State, 'state'))
    district = fields.Field(saves_null_values=True, column_name='district',
                            attribute='district', widget=widgets.ForeignKeyWidget(District, 'district'))
    ItemCode = fields.Field(saves_null_values=True, column_name='ItemCode',
                            attribute='ItemCode', widget=widgets.ForeignKeyWidget(ItemCode, 'ItemCode'))
    Item = fields.Field(saves_null_values=True, column_name='Item',
                        attribute='Item', widget=widgets.ForeignKeyWidget(Item, 'Item'))
    quantity = fields.Field(saves_null_values=False, column_name='quantity', attribute='quantity',
                            widget=widgets.CharWidget())
    departmentName = fields.Field(saves_null_values=False, column_name='departmentName',
                                  attribute='departmentName', widget=widgets.CharWidget())
    departmentAddress = fields.Field(saves_null_values=False, column_name='departmentAddress',
                                     attribute='departmentAddress', widget=widgets.CharWidget())
    contactperson = fields.Field(saves_null_values=False, column_name='contactperson',
                                 attribute='contactperson', widget=widgets.CharWidget())
    contactno = fields.Field(saves_null_values=False, column_name='contactno',
                             attribute='contactno', widget=widgets.CharWidget())
    contactEmail = fields.Field(saves_null_values=False, column_name='contactEmail',
                                attribute='contactEmail', widget=widgets.CharWidget())

    class Meta:
        model = DepartmentContactDetails
        fields = ('id', 'district', 'ItemCode', 'Item', 'quantity',
                  'departmentName', 'departmentAddress', 'contactperson', 'contactno', 'contactEmail')
        clean_model_instances = True


class ItemDescriptionResource(resources.ModelResource):
    id = fields.Field(saves_null_values=False, column_name='id', attribute='id',
                      widget=widgets.IntegerWidget())
    item_desc = fields.Field(saves_null_values=True, column_name='item_dec', attribute='item_desc',
                             widget=widgets.CharWidget())
    location = fields.Field(saves_null_values=True, column_name='location', attribute='location',
                            widget=widgets.CharWidget())
    item_live_location_source = fields.Field(saves_null_values=True, column_name='item_live_location_source', attribute='item_live_location_source',
                            widget=widgets.CharWidget())
    last_updation = fields.Field(saves_null_values=True, column_name='last_updation', attribute='last_updation',
                                 widget=widgets.DateWidget())

    class Meta:
        model = ItemDescription
        clean_model_instances = True



