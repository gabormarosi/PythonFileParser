import pika
import datetime
import os

try:
    filepath = os.environ['PARSER_PATH']
    credentials = pika.PlainCredentials(os.environ['PARSER_USERNAME'],
                                        os.environ['PARSER_PASSWORD'])
    connection = pika.BlockingConnection(pika.ConnectionParameters(os.environ['PARSER_HOSTNAME'],
                                                                   os.environ['PARSER_PORT'],
                                                                   '/',
                                                                   credentials))
    channel = connection.channel()
    channel.queue_declare(queue=os.environ['PARSER_QUEUE_NAME'])
    with open(filepath) as fp:
        line = fp.readline()
        print("Header:"+line.strip())
        print(datetime.datetime.now())
        line = fp.readline()
        while line:
            channel.basic_publish(exchange='',
                                  routing_key=os.environ['PARSER_QUEUE_NAME'],
                                  body=line.strip())
            line = fp.readline()
finally:
    print(datetime.datetime.now())
    connection.close()
    fp.close()