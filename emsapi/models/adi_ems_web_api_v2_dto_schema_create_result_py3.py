# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoSchemaCreateResult(Model):
    """Represents the result of an update.

    All required parameters must be populated in order to send to Azure.

    :param rows_added: Required. The number of rows added by the creation.
    :type rows_added: int
    """

    _validation = {
        'rows_added': {'required': True},
    }

    _attribute_map = {
        'rows_added': {'key': 'rowsAdded', 'type': 'int'},
    }

    def __init__(self, *, rows_added: int, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoSchemaCreateResult, self).__init__(**kwargs)
        self.rows_added = rows_added