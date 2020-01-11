# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AdiEmsWebApiV2ModelAnalyticQueryResult(Model):
    """Represents the time-series data result of an analytic query.

    All required parameters must be populated in order to send to Azure.

    :param offsets: Required. An array of query result offsets, each
     representing seconds from the start of the data
    :type offsets: list[float]
    :param results: Required. An array of analytic result values for each of
     the analytics selected in the query containing values for
     each offset
    :type results:
     list[~emsapi.models.AdiEmsWebApiV2ModelAnalyticAnalyticResult]
    """

    _validation = {
        'offsets': {'required': True},
        'results': {'required': True},
    }

    _attribute_map = {
        'offsets': {'key': 'offsets', 'type': '[float]'},
        'results': {'key': 'results', 'type': '[AdiEmsWebApiV2ModelAnalyticAnalyticResult]'},
    }

    def __init__(self, *, offsets, results, **kwargs) -> None:
        super(AdiEmsWebApiV2ModelAnalyticQueryResult, self).__init__(**kwargs)
        self.offsets = offsets
        self.results = results