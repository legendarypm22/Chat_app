from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person

BUFSIZ = 512

def broadcast():


def client_communication(person):

    """
    Thread to handle all messages from client
    :param person:
    :param client: Person
    :return:None
    """
    run = True
    client = person.client
    name = person.name
    addr = person.addr
    while True:
        msg = client.recv(BUFSIZ)
        if msg != bytes("{quit}", "utf8"):
            client.close()
        else:




def wait_for_connection():
    """
    Wait for connection from new clients, start new thread
    :param SERVER: SOCKET
    :return:None
    """
    run() = True
    while run:
       person, addr = SERVER.accept
       person = Person(addr, client)
       print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
        Thread(target=client_communication, args=(person,))start()
    except Exception as e:
        print("[FAILURE]", e)
        run = False

        print("SERVER CRASHED!")


HOST = 'localhost'
PORT = 5500
ADRR = (HOST,PORT)
MAX_CONNECTIONS = 10

SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADRR)

if__name__=='__main__':
    SERVER.listen(MAX_CONNECTIONS)
    print("[STARTED]Waiting for connection...")
    ACCEPT_THREAD = Thread(target= wait_for_connections(SERVER,))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()
