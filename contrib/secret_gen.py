#!/usr/bin/env python
"""
Django SECRET_KEY generator.
https://gist.github.com/henriquebastos/11cf99c1bbc70bacf73a
"""
from django.utils.crypto import get_random_string


chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
print(get_random_string(50, chars))
