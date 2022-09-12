import pika


connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', blocked_connection_timeout=300))
channel = connection.channel()

def publish(body):
    channel.basic_publish(exchange='', routing_key='qos', body=body)