# -*- coding: utf-8 -*-
"""
Created on Mon Jan 11 12:28:19 2021

@author: Saurabh
"""

import razorpay
import rzkeys
from flask import Flask, render_template, request
from random import randint
from datetime import datetime
import insertTransaction

# Flask Object
app = Flask(__name__)

# Create a razorpay client
client = razorpay.Client(auth=(rzkeys.r_id, rzkeys.r_key))

# Home page to accept transaction details
@app.route('/')
def home_page():
    return render_template ('home.html')


def create_order(amt, descr): 
    order_currency = 'INR'
    
    # create receipt id from random number
    order_receipt = 'receipt_' + str(randint(1,1000))
    
    notes = {'description'   : descr}
    
    data = {'amount'    : amt,
            'currency'  : order_currency,
            'receipt'   : order_receipt,
            'notes'     : notes
        }
    
    response = client.order.create(data)
    order_id = response['id']
    return order_id

@app.route('/submit', methods = ['POST'])
def app_submit():
    amt_d = request.form['amt']
    amt = int(float(amt_d)*100)
    descr = request.form['orderDescr']
    fname = request.form['fname']
    lname = request.form['lname']
    cust_name = fname + " " + lname
  
    c_name = "My First Company"
    
    # create an order for transction before payment
    order_id = create_order(amt, descr)
        
    return render_template('checkout.html', 
                           custName=cust_name,
                           descr=descr,
                           amtD=amt_d,
                           amt=amt,
                           key=rzkeys.r_id,
                           currency='INR',
                           name=c_name,
                           orderId=order_id
                           )

@app.route('/status', methods=['POST'])
def app_status():
    payment_id = request.form['razorpay_payment_id']
    payment_details = client.payment.fetch(payment_id)
    
    payment_details['amount'] = float(payment_details['amount']/100)
    payment_details['amount_refunded'] = float(payment_details['amount_refunded']/100)
    payment_details['created_at'] = datetime.fromtimestamp(payment_details['created_at'])
    
    db_status = insertTransaction.insert_rec(**payment_details)
    
    if db_status == 0:
        return 'Payment transaction details saved in database.'
    else:
        return db_status
    
    return request.form


if __name__=='__main__':
    app.run()










