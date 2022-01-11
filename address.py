#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:39:02 2021

@author: matthew blair
"""
##pip install web3 for this to work

from eth_account import Account
import secrets

vanity = str('0x')
vanity += ('0000') ## Enter hex here
print("Running...")
            
while True:
    priv = secrets.token_hex(32)
    privateKey = "0x" + priv
    account = Account.from_key(privateKey)
    if account.address.startswith(vanity):
        print("Address:", account.address)
        print ("Private Key:", privateKey)
        break
        
