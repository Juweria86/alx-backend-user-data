#!/usr/bin/env python3
""" doc doc doc """

from db import DB
from user import User
import bcrypt
from sqlalchemy.orm.exc import NoResultFound
import uuid
from typing import TypeVar


def _hash_password(password: str) -> bytes:
    """doc doc doc"""
    return bcrypt.hashpw(password.encode(), bcrypt.gensalt())
