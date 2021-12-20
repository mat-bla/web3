#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Dec 20 14:39:02 2021

@author: matthew blair
"""
##pip install web3 for this to work

from eth_account import Account
import secrets

print("Each extra character increases runtime 10x")
vanity = str(input("Enter any numbers or letters (a-f) : "))
print("Running...")

while True:
    priv = secrets.token_hex(32)
    if priv.startswith(vanity) == True:
        privateKey = "0x" + priv
        print ("Private Key:", privateKey)
        account = Account.from_key(privateKey)
        print("Address:", account.address)
        break
        
        
    
    
