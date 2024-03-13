from celery import shared_task
from django.core.mail import send_mail
from orders.models import Order


@shared_task
def order_created(order_id):
    order = Order.objects.get(id=order_id)
    subject = f'Order nr. {order.id}'
    message = 'Dear {}, \n\n' \
              'You have successfully placed an order.' \
              'Your order ID is {}.'.format(order.first_name, order.id)

    mail_sent = send_mail(subject, message, 'admin@mega_shop.com', [order.email])
    return mail_sent
