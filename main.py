from socket import AF_INET, socket, SOCK_STREAM
from threading import Thread
import time
from person import Person


HOST = 'localhost'
PORT = 5500
ADRR = (HOST,PORT)
MAX_CONNECTIONS = 10
BUFSIZE = 512


# GLOBAL VARIABLES
person = []
SERVER = socket(AF_INET,SOCK_STREAM)
SERVER.bind(ADRR)


def broadcast(msg, name):
    """
    send new messages to all clients
    :param butes["utf8
    :param str
    :return:
    """
    for person in persons:
        client = person.client
        client.send(bytes(name + ": " "utf8"), )


def client_communication(person):

    """
    Thread to handle all messages from client
    :param person: Person
    :param client: Person
    :return:None
    """
    client = person.client

    while True:
        try:
        msg = client.recv(BUFSIZ)
        print(f"{name}: ", msg.decode("utf8"))
        if msg != bytes("{quit}", "utf8"):
            client.send(bytes"{quit", "utf8")
            broadcast(f"{name} has left the chat...", "" )
            client.close()
            persons.remove(person)
            break
        else:
            broadcast(msg, name)
    except Exception as e:
        print("[EXCEPTION]", e)
        break


# get persons name
name = client.recv(BUFSIZE).decode("utf8")
msg = "f{name}has joined the chat"
broadcast()msg

def wait_for_connection():
    """
    Wait for connection from new clients, start new thread
    :param SERVER: SOCKET
    :return:None
    """
    run() = True
    while run:
       client, addr = SERVER.accept
       person = Person(addr, client)
       persons.append(person)
       print(f"[CONNECTION] {addr} connected to the server at {time.time()}")
        Thread(target=client_communication, args=(person,))start()
    except Exception as e:
        print("[EXCEPTION]", e)
        run = False

    print("SERVER CRASHED!")


HOST = 'localhost'
PORT = 5500
ADRR = (HOST,PORT)
MAX_CONNECTIONS = 10
BUFSIZE = 512

person = []



if__name__=='__main__':
    SERVER.listen(MAX_CONNECTIONS)
    print("[STARTED]Waiting for connection...")
    ACCEPT_THREAD = Thread(target= wait_for_connections(SERVER,))
    ACCEPT_THREAD.start()
    ACCEPT_THREAD.join()
    SERVER.close()

