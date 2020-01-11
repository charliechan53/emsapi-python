# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaOrderByColumn(Model):
    """Represents a column of data that can be used in a order-by clause of a data
    source query.

    All required parameters must be populated in order to send to Azure.

    :param field_id: Required. The unique string identifier of the field to
     use in a order-by clause of a query
    :type field_id: str
    :param aggregate: An optional aggregate operation to perform on the
     column. Omission of this property results in no aggregate
     operation being used in the ordering. Possible values include: 'none',
     'avg', 'count', 'max', 'min', 'stdev', 'sum', 'var'
    :type aggregate: str or ~emsapi.models.enum
    :param order: The ordering behavior to use for the column values. The
     omission of this property results in ascending order. Possible values
     include: 'asc', 'desc'
    :type order: str or ~emsapi.models.enum
    """

    _validation = {
        'field_id': {'required': True},
    }

    _attribute_map = {
        'field_id': {'key': 'fieldId', 'type': 'str'},
        'aggregate': {'key': 'aggregate', 'type': 'str'},
        'order': {'key': 'order', 'type': 'str'},
    }

    def __init__(self, *, field_id: str, aggregate=None, order=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoSchemaOrderByColumn, self).__init__(**kwargs)
        self.field_id = field_id
        self.aggregate = aggregate
        self.order = order