import contextlib
import socket
import logging

logger = logging.getLogger()


# in the following code there are 2 things that need modification:
# 1. the socket must be closed in any circumstances in order to not leak its resource
# 2. log_event should pass successfully in case nice_to_have_send_message fails with ConnectionError since its a
#    nice-to-have logging the event to remote server... (notice that in other error cases it should fail)

def nice_to_have_send_message(message):

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        s.connect(("127.0.0.1", 5050))
        s.sendall(message.encode())
    finally:
        s.close()

    # better impl
    # with socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    #     s.connect(("1.2.3.4", 5050))
    #     s.sendall(message.encode())


def log_event(message):
    print(message)
    logger.info(message)

    try:
        nice_to_have_send_message(message)
    except ConnectionError:
        pass

    # better impl
    # with contextlib.suppress(ConnectionError):
    #     nice_to_have_send_message(message)

log_event("hello world")
