""" Backend service """
import logging
from jsonrpclib.SimpleJSONRPCServer import SimpleJSONRPCServer
import operations
# import json 
# import os 
# import sys

# from bson.json_util import dumps
# sys.path.append(os.path.join(os.path.dirname(__file__), 'utils')) 
# import mongodb_client

SERVER_HOST = 'localhost'
SERVER_PORT = 4040

LOGGER_FORMAT = '%(asctime)s - %(message)s'
logging.basicConfig(format=LOGGER_FORMAT)
LOGGER = logging.getLogger('backend_service')
LOGGER.setLevel(logging.DEBUG)


def add(num1, num2):
    """ Test method """
    LOGGER.debug("add is called with %d and %d", num1, num2)
    return num1 + num2


def get_one_news():
    """ Test method to get one news """
    LOGGER.debug("getOneNews is called")
    return operations.getOneNews()

# def getOneNews():
# 	LOGGER.debug("getOneNews is called")
# 	res = mongodb_client.get_db()['news'].find_one() # dumps(res): convert bson to string
# 	# then convert string to json
# 	return json.loads(dumps(res))


# Threading RPC Server
RPC_SERVER = SimpleJSONRPCServer((SERVER_HOST, SERVER_PORT))
RPC_SERVER.register_function(add, 'add')
RPC_SERVER.register_function(get_one_news, 'getOneNews')

LOGGER.info("Starting RPC server on %s:%d", SERVER_HOST, SERVER_PORT)

RPC_SERVER.serve_forever()


