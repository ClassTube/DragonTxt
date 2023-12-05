#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# (c) ACE 

import os

class Config(object):
    # get a token from @BotFather
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6917084113:AAFOK37UIoEQLtY2HYu5UeF77cIF4BfGnwk")
    API_ID = int(os.environ.get("API_ID", "27097807"))
    API_HASH = os.environ.get("API_HASH", "9fd790a9cb1f639c921d941621d2959d")
