import socket
import logging

logger = logging.getLogger()


# in the following code there are 2 things that need modification:
# 1. the socket must be closed in any circumstances in order to not leak its resource
# 2. log_event should pass successfully in case nice_to_have_send_message fails with ConnectionError since its a
#    nice-to-have logging the event to remote server... (notice that in other error cases it should fail)

def nice_to_have_send_message(message):

    raise NotImplementedError("YOUR IMPLEMENTATION HERE")

    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 5050))
    s.sendall(message.encode())
    s.close


def log_event(message):

    print(message)
    logger.info(message)

    raise NotImplementedError("YOUR IMPLEMENTATION HERE")
    nice_to_have_send_message(message)


log_event("hello world")
