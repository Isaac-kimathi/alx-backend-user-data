#!/usr/bin/env python3
"""module for class BasicAuth"""

import re
import base64
import binascii
from typing import Tuple, TypeVar

from api.v1.auth.auth import Auth
from models.user import User

class BasicAuth(Auth):
    """Baic authentication class.
    """
    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """returns base64 part of authorization header for for a Basic Authentication"""
        if type(authorization_header) == str:
            pattern = pattern = r'Basic (?P<token>.+)'
            field_match = re.fullmatch(pattern, authorization_header.strip())
            if field_match is not None:
                return field_match.group('token')

        return None

    def decode_base64_authorization_header(self, base64_authorization_header: str) -> str:
        """returns the decoded value of a Base64 string"""
        if type(base64_authorization_header) == str:
            try:
                res = base64.b64decode(
                        base64_authorization_header,
                        validate=True,
                        )
                return res.decode('utf-8')
            except (binascii.Error, UnicodeDecodeError):
                return None

    def extract_user_credentials(self, decoded_base64_authorization_header: str,) -> Tuple[str, str]:
            """returns the user email and password from the Base64 decoded value"""
            if type(decoded_base64_authorization_header) == str:
                pattern = r'(?P<user>[^:]+):(?P<password>.+)'
                field_match = re.fullmatch(
                        pattern, 
                        decoded_base64_authorization_header.strip(),
                )
                if field_match is not None:
                    user = field_match.group('user')
                    password = field_match.group('password')
                    return user, password
            return None, None
