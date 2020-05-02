"""
This module contains the server-side code for accepting a payment with Stripe.
"""
import json
import os

import stripe
from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api

stripe.api_key = os.environ.get('STRIPE_API_KEY')



class PaymentIntent(Resource):
    """Endpoint for creating payment intent objects

    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """
    # TODO replace receipt_email with the parent's email address
    def post(self):
        try:
            data = json.loads(request.data)
            intent = stripe.PaymentIntent.create(
                amount=calculate_order_amount(data['items']),
                currency='usd',
                payment_method_types=["card"],
                receipt_email="bear.davis@example.com"
            )
            return jsonify({
              'clientSecret': intent['client_secret']
            })
        except Exception as e:
            return jsonify(error=str(e)), 403


def calculate_order_amount(items):
    # TODO Replace this lgic with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    price = len(items) * 111
    return price
