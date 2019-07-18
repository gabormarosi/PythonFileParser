import pika
import datetime

try:
    filepath = '/Users/gmarosi/main/trx.csv'
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rtd.dwh.transaction')
    with open(filepath) as fp:
        line = fp.readline()
        print("Header:"+line.strip())
        print(datetime.datetime.now())
        line = fp.readline()
        while line:
            channel.basic_publish(exchange='',
                                  routing_key='rtd.dwh.transaction',
                                  body=line.strip())
            line = fp.readline()
finally:
    print(datetime.datetime.now())
    connection.close()
    fp.close()