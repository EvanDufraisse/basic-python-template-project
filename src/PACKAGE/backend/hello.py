# -*- coding: utf-8 -*-
""" Hello World function

@Author: Evan Dufraisse
@Date: Wed Oct 02 2024
@Contact: evan[dot]dufraisse[at]cea[dot]fr
@License: Copyright (c) 2024 CEA - LASTI
"""

def print_hello_name(name, allcaps=False):
    if allcaps:
        print(f"HELLO {name.upper()}!")
    else:
        print(f"Hello {name}!")