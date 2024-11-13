#!/usr/bin/env python3
"""
module of a class to manage the API authentication
"""
from flask import request
from typing import List, TypeVar

class Auth:
    """class to manage the API authenication
    """
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        public methd to authenticate path
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        method to extract authorization header from the request object
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None

        return request.headers.get('Authorization')

    def current_user(self, request=None) -> TypeVar('User'):
        """
        method of retrieve the current user based on the request
        """
        return None
