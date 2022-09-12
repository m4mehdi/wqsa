from os import environ
from sys import path
import django

path.append('Users/Matin/OneDrive/Desktop/Dars/Courses/Django/VSCode/web_project/web_project/settings.py') 
environ.setdefault('DJANGO_SETTINGS_MODULE', 'web_project.settings')
django.setup()

import pika
from web_api.views import QualityApiView
from web_api.serializers import QualitySerializer



connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', heartbeat=600, blocked_connection_timeout=300))
channel = connection.channel()
channel.queue_declare(queue='qos')

def callback(ch, method, properties, body):
    data = body
    data = data.decode()
    print('consumed: ',data)
    response = {'ip':data}
    response = QualitySerializer(response)
    x = QualityApiView()
    x.post(request = response)


channel.basic_consume(queue='qos', on_message_callback=callback, auto_ack=True)
print("Started Consuming...")
channel.start_consuming()