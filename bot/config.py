#!/usr/bin/env python3
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License.

import os

""" Bot Configuration """


class DefaultConfig:
    """ Bot Configuration """

    PORT = 3978
    APP_ID = os.environ.get("MicrosoftAppId", "945b3db8-4efd-43fb-b36f-2969a922dcd7")
    APP_PASSWORD = os.environ.get("MicrosoftAppPassword", "02f817f1-2e3f-4304-ae4c-57ea70680a3c")
