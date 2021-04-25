# -*- coding: utf-8 -*-
"""
Created on Sat Jan  9 23:00:11 2021

@author: Saurabh
"""

import razorpay
import rzkeys

client = razorpay.Client(auth=(rzkeys.r_id, rzkeys.r_key))

# data = {'amount' : 999,
#         'currency' : 'USD'}


# response = client.order.create(data)

response = client.payment.fetch('pay_PGwRhg6edaNjZQ')


