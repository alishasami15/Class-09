import random

def generate_payment_link():
    return "https://example.com/payment-gateway"

def process_payment(user_email, amount):
    transaction_id = f"TXN{random. randint(100000, 999999)}"
    return {
        "status" : "success",
        "user":user_email,
        "amount": amount,
        "transaction_id": transaction_id    
        }