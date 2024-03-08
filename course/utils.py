import stripe
from config.settings import API_KEY
from users.models import Client


def create_product(client):
    stripe.api_key = API_KEY
    product = stripe.Product.create(name=client.courses.name)

    product_price = stripe.Price.create(
        currency="usd",
        unit_amount=1000,
        product_data={"name": product.get('name')}
    )

    product_url = stripe.checkout.Session.create(
        success_url="http://127.0.0.1:8000/",
        line_items=[{"price": product_price.get('id'), "quantity": 1}],
        mode="payment",
    )
    return product_url['url']
