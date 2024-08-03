#!/usr/bin/env python3
""""module doc"""
import re
from typing import List
import logging


def filter_datum(
    fields: List[str], redaction: str, message: str, separator: str
) -> str:
    """"returns the log message obfuscated"""
    pattern = '|'.join([f'(?<={field}=)[^{separator}]+' for field in fields])
    return re.sub(pattern, redaction, message)


class RedactingFormatter(logging.Formatter):
    """doc doc doc"""

    REDACTION = "***"
    FORMAT = "[HOLBERTON] %(name)s %(levelname)s %(asctime)-15s: %(message)s"
    SEPARATOR = ";"

    def __init__(self, fields: List[str]):
        """doc doc doc"""
        super(RedactingFormatter, self).__init__(self.FORMAT)
        self.fields = fields

    def format(self, record: logging.LogRecord) -> str:
        """func doc"""
        org = super().format(record)
        return filter_datum(self.fields, self.REDACTION, org, self.SEPARATOR)


PII_FIELDS = ("name", "email", "phone", "ssn", "password")
