# alligator_def/__init__.py
########################################
#                                      #
#     DO NOT MODIFY THIS FILE !!!      #
#                                      #
########################################
# This file is used to load the proper AlliGator data structure definitions
# when an "import alligator_def" statement is found in a plugin function
# last modified: 2026-10-21 by XM


import os

# Read requested version from environment variable (defaults to '1.1.1')
ALLIGATOR_DEFINITIONS_VERSION = os.getenv("ALLIGATOR_DEFINITIONS_VERSION", "1.1.1").lower()

if ALLIGATOR_DEFINITIONS_VERSION == "1.1.1":
    from .alligator_def_v1_1_1 import *
else:
    raise ValueError(f"Unknown definitions version: {ALLIGATOR_DEFINITIONS_VERSION}")
    
