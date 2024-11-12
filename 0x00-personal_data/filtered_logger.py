#!/usr/bin/env python3
"""
Script for handling personal data
"""
from typing import List
import re
import logging


# # PII fields to be redacted
PII_FIELDS = ("name", "email", "phone", "ssn", "password")


def filter_datum(fields: List[str], redaction: str,
                         message: str, separator: str) -> str:
    """
    Replaces sensitive information in a message with a redacted value
    based on the list of fields to obfuscate

    Args:
        fields: list of fields to redact
        redaction: the value to use for redaction
        message: the string message to filter
        separator: the separator to use between fields

    Returns:
        The filtered string message with redacted values
    """
    for f in fields:
        message = re.sub(f'{f}=.*?{separator}',
                f'{f}={redaction}{separator}', message)
    return message

class RedactingFormatter(logging.Formatter):
    """Redacting Formatter class"""
    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self):
        """innitializes the super class"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def 
