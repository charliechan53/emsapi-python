# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoWeatherTafIcingCondition(Model):
    """Describes a forecast icing condition.

    :param intensity: The intensity code associated with the icing. Uses the
     following values:
     0 - Trace icing or none,
     1 - Light mixed icing,
     2 - Light rime icing in cloud,
     3 - Light clear icing in precipitation,
     4 - Moderate mixed icing,
     5 - Moderate rime icing in cloud,
     6 - Moderate clear icing in precipitation,
     7 - Severe mixed icing,
     8 - Severe rime icing in cloud,
     9 - Severe clear icing in precipitation
    :type intensity: int
    :param minimum: The base limit of the icing layer in feet
    :type minimum: int
    :param maximum: The top limit of the icing layer in feet
    :type maximum: int
    """

    _attribute_map = {
        'intensity': {'key': 'intensity', 'type': 'int'},
        'minimum': {'key': 'minimum', 'type': 'int'},
        'maximum': {'key': 'maximum', 'type': 'int'},
    }

    def __init__(self, **kwargs):
        super(AdiEmsWebApiV2DtoWeatherTafIcingCondition, self).__init__(**kwargs)
        self.intensity = kwargs.get('intensity', None)
        self.minimum = kwargs.get('minimum', None)
        self.maximum = kwargs.get('maximum', None)
