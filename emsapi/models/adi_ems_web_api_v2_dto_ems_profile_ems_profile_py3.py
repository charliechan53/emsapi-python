# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoEmsProfileEmsProfile(Model):
    """Represents an APM (Automated Parameter Measurement) profile in an EMS
    system.

    All required parameters must be populated in order to send to Azure.

    :param profile_id: Required. The local identifier for a profile
    :type profile_id: int
    :param profile_guid: Required. The unique identifier of a profile in the
     system
    :type profile_guid: str
    :param profile_name: Required. The name of the profile
    :type profile_name: str
    :param library: Required. Flag for if a profile is a library profile
    :type library: bool
    :param current_version: Required. The version of the profile
    :type current_version: int
    :param path: Required. Path to the profile's location
    :type path: str
    """

    _validation = {
        'profile_id': {'required': True},
        'profile_guid': {'required': True},
        'profile_name': {'required': True},
        'library': {'required': True},
        'current_version': {'required': True},
        'path': {'required': True},
    }

    _attribute_map = {
        'profile_id': {'key': 'profileId', 'type': 'int'},
        'profile_guid': {'key': 'profileGuid', 'type': 'str'},
        'profile_name': {'key': 'profileName', 'type': 'str'},
        'library': {'key': 'library', 'type': 'bool'},
        'current_version': {'key': 'currentVersion', 'type': 'int'},
        'path': {'key': 'path', 'type': 'str'},
    }

    def __init__(self, *, profile_id: int, profile_guid: str, profile_name: str, library: bool, current_version: int, path: str, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoEmsProfileEmsProfile, self).__init__(**kwargs)
        self.profile_id = profile_id
        self.profile_guid = profile_guid
        self.profile_name = profile_name
        self.library = library
        self.current_version = current_version
        self.path = path
