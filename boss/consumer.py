import pika 

params = pika.URLParameters('amqps://igqylvwy:TcwMgVG-nqWB4Riz7lSMPp17hEg3qOAC@vulture.rmq.cloudamqp.com/igqylvwy')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='boss')

def callback(ch, method, properties, body):
    print('Received in boss')
    print(body)

channel.basic_consume(queue='boss', on_message_callback=callback)

print('Started consuming')

channel.start_consuming()

channel.close()