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
        return false

    def authorization_header(self, request=None) -> str:
        """
        method to extract authorization header from the request object
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        method of retrieve the current user based on the request
        """
        return None
