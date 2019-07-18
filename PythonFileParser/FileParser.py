import pika
import datetime

try:
    filepath = '/Users/gmarosi/main/teszt.csv'
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='rtd.dwh.transaction')
    with open(filepath) as fp:
        line = fp.readline()
        cnt = 1
        print("Header:"+line.strip())
        print(datetime.datetime.now())
        line = fp.readline()
        while line:
            #print("Line {}: {}".format(cnt, line.strip()))
            channel.basic_publish(exchange='',
                                  routing_key='rtd.dwh.transaction',
                                  body=line.strip())
            line = fp.readline()
            cnt += 1
finally:
    print(datetime.datetime.now())
    connection.close()
    fp.close()