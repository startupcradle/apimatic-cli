# -*- coding: utf-8 -*-

"""
    apimatic.controllers.generator_controller

    This file was automatically generated by APIMATIC v2.0 ( https://apimatic.io ).
"""

from .base_controller import BaseController
from ..api_helper import APIHelper
from ..configuration import Configuration
from ..http.auth.custom_header_auth import CustomHeaderAuth

class GeneratorController(BaseController):

    """A Controller to access Endpoints in the apimatic API."""


    def generate_from_url(self,
                          name,
                          description_url,
                          template):
        """Does a GET request to /codegen.

        Generates SDK given an API description URL.

        Args:
            name (string): TODO: type description here. Example: 
            description_url (string): TODO: type description here. Example: 
            template (string): TODO: type description here. Example:
                cs_portable_net_lib

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'name': name,
            'descriptionUrl': description_url,
            'template': template
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def generate_from_file(self,
                           name,
                           file,
                           template):
        """Does a POST request to /codegen.

        Generates SDK given an API description file.

        Args:
            name (string): TODO: type description here. Example: {abc}
            file (string): TODO: type description here. Example: 
            template (string): TODO: type description here. Example:
                cs_portable_net_lib

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'name': name,
            'template': template
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare files
        _files = {
            'file': file
        }

        # Prepare and execute request
        _request = self.http_client.post(_query_url, files=_files)
        CustomHeaderAuth.apply(_request)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body

    def generate_from_key(self,
                          apikey,
                          template):
        """Does a GET request to /codegen.

        Generates SDK given an API key.

        Args:
            apikey (string): The API key from APIMatic
            template (string): TODO: type description here. Example:
                cs_portable_net_lib

        Returns:
            string: Response from the API. 

        Raises:
            APIException: When an error occurs while fetching the data from
                the remote API. This exception includes the HTTP Response
                code, an error message, and the HTTP body that was received in
                the request.

        """

        # Prepare query URL
        _query_builder = Configuration.base_uri
        _query_builder += '/codegen'
        _query_parameters = {
            'apikey': apikey,
            'template': template
        }
        _query_builder = APIHelper.append_url_with_query_parameters(_query_builder,
            _query_parameters, Configuration.array_serialization)
        _query_url = APIHelper.clean_url(_query_builder)

        # Prepare and execute request
        _request = self.http_client.get(_query_url)
        _context = self.execute_request(_request)
        self.validate_response(_context)

        # Return appropriate type
        return _context.response.raw_body
