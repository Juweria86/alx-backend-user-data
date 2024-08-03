#!/usr/bin/env python3
""" returns a salted, hashed password """
import bcrypt


def hash_password(password: str) -> bytes:
    """doc doc doc"""
    return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())


def is_valid(hashed_password: bytes, password: str) -> bool:
    """func doc"""
    return bcrypt.checkpw(password.encode("utf-8"), hashed_password)