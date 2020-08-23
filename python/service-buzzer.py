import rabbitpy
from time import sleep
from gpiozero import Buzzer
from retrying import retry


buzzer = Buzzer(7)
amqp_uri = 'URI_HERE'


@retry(wait_exponential_multiplier=1000, wait_exponential_max=10000)
def connecting():
    try:
        print('Trying to connect to rmq...')
        return rabbitpy.Connection(amqp_uri)
    except rabbitpy.exceptions.ConnectionException:
        print('Failed to connect. Retrying...')
        raise


with connecting() as conn:
    print('connected to rabbitmq')
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel, 'q_pi_buzzer')

        try:
            for message in queue:
                buzzer.on()
                sleep(1)
                buzzer.off()
                sleep(1)
                message.ack()
        except rabbitpy.exceptions.AMQPException:
            print('Exited consumer')
