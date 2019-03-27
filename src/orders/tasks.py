from celery import task
from django.core.mail import send_mail
from celery import Celery


app = Celery('tasks', backend='amqp', broker='amqp://guest:guest@localhost:5672//')

@app.task
def OrderCreated(order_id):
    from orders.models import Order
    """
    Отправка Email сообщения о создании покупке
    """
    order = Order.objects.get(id=order_id)
    subject = 'Замовлення №{}, Pasta Family'.format(order.id)
    message_1 = """Спасибі за замовлення.  У вас чудовий смак.
    
Після підтвердження оплати та відправлення, вам на пошту прийде номер накладної.
———————————————
Замовлення оформлені до 16:00(у робочі дні) відправляються в той же день, після 16:00 - на наступний.
    
    
Якшо виникли якісь запитання, напишіть нам на пошту PastaFamily.officе@gmail.com, або телефонуйте за номером: 096-144-38-88, 095-744-38-88
З найкращими побажаннями, команда Pasta Family. http://pasta-family.com.ua
                    """
    message_2 = """Спасибі за замовлення.  У вас чудовий смак.
    
Сума* до сплати {} грн.
    
*вказана сума без урахування банківської комісії.

Реквізити для оплати замовлення:
4149 4991 0980 4680
Ксьонжик Володимир

ОБОВ‘ЯЗКОВО в призначенні платежу вкажіть номер замовлення.
    
Після відправлення товару, вам на пошту прийде номер накладної.
———————————————
Замовлення оформлені до 16:00(у робочі дні) відправляються в той же день, після 16:00 - на наступний.
    
    
Якшо виникли якісь запитання, напишіть нам на пошту PastaFamily.officе@gmail.com, або телефонуйте за номером: 096-144-38-88, 095-744-38-88
З найкращими побажаннями, команда Pasta Family. http://pasta-family.com.ua
                        """.format(order.get_total_cost())
    message_3 = """Спасибі за замовлення.  У вас чудовий смак.

Після відправки вам на пошту прийде номер накладної
———————————————
Замовлення оформлені до 16:00(у робочі дні) відправляються в той же день, після 16:00 - на наступний.
    
    
Якшо виникли якісь запитання, напишіть нам на пошту PastaFamily.officе@gmail.com, або телефонуйте за номером: 096-144-38-88, 095-744-38-88
З найкращими побажаннями, команда Pasta Family. http://pasta-family.com.ua
                        """
    if order.payment_method.id == 1:
        mail_send = send_mail(subject, message_1, 'pastafamily.office@gmail.com', [order.email])
    elif order.payment_method.id == 2:
        mail_send = send_mail(subject, message_2, 'pastafamily.office@gmail.com', [order.email])
    elif order.payment_method.id == 3:
        mail_send = send_mail(subject, message_3, 'pastafamily.office@gmail.com', [order.email])
    return mail_send


@app.task
def OrderSend(order_id):
    from orders.models import Order
    """
    Отправка Email сообщения о создании покупке
    """
    order = Order.objects.get(id=order_id)
    subject = 'Ваше замовлення №{}, уже їде до вас. Pasta Family'.format(order.id)
    message = """Спасибі за замовлення.  У вас чудовий смак.

Номер накладної: {}

Відгук можете залишити за посиланням: http://pasta-family.com.ua/review

З найкращими побажаннями, команда Pasta Family. http://pasta-family.com.ua
                    """.format(order.declaration)

    mail_send = send_mail(subject, message, 'pastafamily.office@gmail.com', [order.email])
    return mail_send
