# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2DtoAssetAirport(Model):
    """Encapsulates the definition of an airport.

    :param id: The identifier of the airport within the system.
    :type id: int
    :param code_iata: The IATA code associated with this airport.
    :type code_iata: str
    :param code_icao: The ICAO code associated with this airport.
    :type code_icao: str
    :param code_faa: The FAA / Regional code associated with this airport.
    :type code_faa: str
    :param code_preferred: The preferred code to use for display. This is
     typically either the ICAO or FAA code, but can be overridden by the user.
    :type code_preferred: str
    :param name: The name of the airport.
    :type name: str
    :param city: The city of the airport.
    :type city: str
    :param country: The country of the airport.
    :type country: str
    :param latitude: The latitude of the airport.
    :type latitude: float
    :param longitude: The longitude of the airport.
    :type longitude: float
    :param elevation: The elevation of the airport, in feet.
    :type elevation: float
    """

    _attribute_map = {
        'id': {'key': 'id', 'type': 'int'},
        'code_iata': {'key': 'codeIata', 'type': 'str'},
        'code_icao': {'key': 'codeIcao', 'type': 'str'},
        'code_faa': {'key': 'codeFaa', 'type': 'str'},
        'code_preferred': {'key': 'codePreferred', 'type': 'str'},
        'name': {'key': 'name', 'type': 'str'},
        'city': {'key': 'city', 'type': 'str'},
        'country': {'key': 'country', 'type': 'str'},
        'latitude': {'key': 'latitude', 'type': 'float'},
        'longitude': {'key': 'longitude', 'type': 'float'},
        'elevation': {'key': 'elevation', 'type': 'float'},
    }

    def __init__(self, *, id: int=None, code_iata: str=None, code_icao: str=None, code_faa: str=None, code_preferred: str=None, name: str=None, city: str=None, country: str=None, latitude: float=None, longitude: float=None, elevation: float=None, **kwargs) -> None:
        super(AdiEmsWebApiV2DtoAssetAirport, self).__init__(**kwargs)
        self.id = id
        self.code_iata = code_iata
        self.code_icao = code_icao
        self.code_faa = code_faa
        self.code_preferred = code_preferred
        self.name = name
        self.city = city
        self.country = country
        self.latitude = latitude
        self.longitude = longitude
        self.elevation = elevation
