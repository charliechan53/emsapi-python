# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoMetadataItem(Model):
    """Encapsulates a single piece of metadata.

    :param key: The metadata key.
    :type key: str
    :param value: The metadata value.
    :type value: object
    """

    _attribute_map = {
        'key': {'key': 'key', 'type': 'str'},
        'value': {'key': 'value', 'type': 'object'},
    }

    def __init__(self, *, key: str=None, value=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoMetadataItem, self).__init__(**kwargs)
        self.key = key
        self.value = value
