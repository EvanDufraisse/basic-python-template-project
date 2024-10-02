#!/usr/bin/python
# -*- coding: utf-8 -*-
""" Example import in a library


@Author: Evan Dufraisse
@Date: Wed Oct 02 2024
@Contact: evan[dot]dufraisse[at]cea[dot]fr
@License: Copyright (c) 2024 CEA - LASTI
"""
import argparse
from PACKAGE.backend.hello import print_hello_name





if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Print your name')

    parser.add_argument('name', type=str, help='Your name')
    parser.add_argument('--allcaps', action='store_true', help='Print name in all caps')

    args = parser.parse_args()