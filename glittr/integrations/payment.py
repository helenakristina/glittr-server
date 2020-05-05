"""
This module contains the server-side code for accepting a payment with Stripe.
"""
import json
import os

import stripe
from flask import Flask, render_template, jsonify, request
from flask_restful import Resource, Api

stripe.api_key = os.environ.get('STRIPE_API_KEY')


def calculate_order_amount(items):
    # TODO Replace this lgic with a calculation of the order's amount
    # Calculate the order total on the server to prevent
    # people from directly manipulating the amount on the client
    price = len(items) * 111
    return price


class StripeWebhook(Resource):
    """Endpoint that can receive requests from Stripe to notify us about
    payment events that happen in the real world outside of our payment
    flow such as:

    Successful payments (payment_intent.succeeded)
    Disputed payments (charge.dispute.created)
    Available balance in your Stripe account (balance.available)

    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """
    def post(self):
        payload = request.data
        event = None
        try:
            event = stripe.Event.construct_from(
              json.loads(payload), stripe.api_key
            )
        except ValueError as e:
            # Invalid payload
            return jsonify(error=str(e)), 400

        # Handle the event
        if event.type == 'payment_intent.succeeded':
            payment_intent = event.data.object # contains a stripe.PaymentIntent
            print('PaymentIntent was successful!')
        elif event.type == 'payment_method.attached':
            payment_method = event.data.object # contains a stripe.PaymentMethod
            print('PaymentMethod was attached to a Customer!')
            # ... handle other event types
        else:
            # Unexpected event type
            print('Unexpected event type!')

        return {"message": "fin :-)"}


class PaymentIntent(Resource):
    """Endpoint for creating payment intent objects

    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """
    # TODO replace receipt_email with the parent's email address
    def post(self):
        try:
            # Create a new Customer before creating a PaymentIntent
            # so we can store the card for future purchases
            customer = stripe.Customer.create()

            data = json.loads(request.data)
            intent = stripe.PaymentIntent.create(
                customer=customer['id'],
                # setup_future_usage tells Stripe how you plan to use the card
                # — certain regions, such as Europe and India, have
                # requirements around reusing card details.
                setup_future_usage='off_session',
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



class ChargeSavedCard(Resource):
    """Endpoint for charging a saved card used in a prior payment

    Arguments:
        Resource {Flask-Restful Resource} -- Resource to use for routing
    """
    def post(self):
        data = json.loads(request.data)
        customer_id = data['customer_id']
        payment_method_id = data['customer_id']

        # Lookup the saved card (you can store multiple PaymentMethods on a Customer)
        payment_methods = stripe.PaymentMethod.list(
            customer=customer_id,
            type='card'
        )
        # Charge the customer and payment method immediately
        # TODO don't just grab the first payment method, grab the one with
        # matching last 4 to what we saved
        payment_intent = stripe.PaymentIntent.create(
            amount=2000,
            currency='usd',
            customer=customer_id,
            payment_method=payment_methods.data[0].id,
            off_session=True,
            confirm=True
        )
        if payment_intent.status == 'succeeded':
            print('Successfully charged card off session')


