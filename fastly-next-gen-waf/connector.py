"""
Copyright start
MIT License
Copyright (c) 2024 Fortinet Inc
Copyright end
"""
from connectors.core.connector import Connector, ConnectorError, get_logger
from .operations import check_health, operations

logger = get_logger('fastly-next-gen-waf')


class FastlyWAFConnector(Connector):

    def execute(self, config, operation, params, *args, **kwargs):
        try:
            return operations.get(operation)(config, params)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(str(err))

    def check_health(self, config=None, *args, **kwargs):
        try:
            return check_health(config)
        except Exception as err:
            logger.exception(err)
            raise ConnectorError(str(err))
