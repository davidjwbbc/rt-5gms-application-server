#!/usr/bin/python3
#
# 5G-MAG Reference Tools: 5GMS Application Server
# ===============================================
#
# File: context.py
# License: 5G-MAG Public License (v1.0)
# Author: David Waring
# Copyright: (C) 2022 British Broadcasting Corporation
#
# For full license terms please see the LICENSE file distributed with this
# program. If this file is missing then the license can be retrieved from
# https://drive.google.com/file/d/1cinCiA778IErENZ3JN52VFW-1ffHpx7Z/view
#
# This is the 5G-MAG Reference Tools 5GMS AS application context module.
# This file handles the class which will hold the current run-time context of
# the AS.
#
'''
5gms_as.context module
======================

This module provides a single Context class which holds the context for the
5G-MAG Reference Tools 5GMS AS Network Function.
'''

import json

from .openapi_5g.model.content_hosting_configuration import ContentHostingConfiguration
from .openapi_5g.model_utils import deserialize_model

class Context(object):
    '''
    Context class
    -------------

    Class to hold and manipulate the current context for the 5G-MAG Reference
    Tools 5GMS AS Network Function.
    '''

    def __init__(self, config_filename):
        '''Constructor

        config_filename (str) - filename of the ContentHostingConfiguration JSON
        '''
        chc = deserialize_model(json.load(open(config_filename, 'r')), ContentHostingConfiguration, config_filename, True, {}, True)
        self.__chcs = {chc.name: chc}

    def contentHostingConfigurations(self):
        '''Get the list of defined ContentHostingConfiguration objects

        Returns a list of the configured ContentHostingConfiguration objects
                associated with the AS.
        '''
        return self.__chcs.values()

    def findContentHostingConfiguration(self, name):
        '''
        Find a named ContentHostingConfiguration

        Return the ContentHostingConfiguration for the given name or None if
        a configuration with that name has not been defined in this context.
        '''
        if name in self.__chcs:
            return self.__chcs[name]
        return None

