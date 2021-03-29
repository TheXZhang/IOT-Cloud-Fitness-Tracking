import psycopg2
import select
import ast
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
from pyfcm import FCMNotification

push_service = FCMNotification(api_key="put FCM api key here")
registration_id = "device id here"
message_title = "Achievement"


connection = psycopg2.connect(dbname='iotssc', user='tester', password='password')

connection.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
cur = connection.cursor()
cur.execute("LISTEN achievement;")
while True:
    select.select([connection], [], [])
    connection.poll()
    events = []
    while connection.notifies:
        notify = connection.notifies.pop().payload
        notify_dict = ast.literal_eval(notify)
        print(notify_dict)

        if notify_dict['running'] == 10:
            print("running 30 achieved")
            message_body = "You have reached running achievement {}".format(10)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                       message_body=message_body)
        if notify_dict['walking'] == 10:
            print("walking 10 achieved")
            message_body = "You have reached walking achievement {}".format(10)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                       message_body=message_body)
        if notify_dict['running'] == 100:
            print("running 10 achieved")
            message_body = "You have reached running achievement {}".format(100)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                       message_body=message_body)
        if notify_dict['walking'] == 100 :
            print("walking 100 achieved")
            message_body = "You have reached walking achievement {}".format(100)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                       message_body=message_body)
        if notify_dict['running'] == 1000 :
            print("running 1000 achieved")
            message_body = "You have reached running achievement {}".format(1000)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                       message_body=message_body)
        if notify_dict['walking'] == 1000:
            print("walking 1000 achieved")
            message_body = "You have reached walking achievement {}".format(1000)
            result = push_service.notify_single_device(registration_id=registration_id, message_title=message_title,
                                                       message_body=message_body)
