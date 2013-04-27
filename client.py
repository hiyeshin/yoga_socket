from twisted.internet import reactor
from twisted.python import log
from autobahn.websocket import WebSocketClientFactory, WebSocketClientProtocol, connectWS
import sys
from rpi_ws.client_protocol import RPIClientProtocol, ReconnectingWebSocketClientFactory
from rpi_ws import settings

USE_SSL = False
PORT = 9000
SERVER = '192.168.0.10'
#SERVER = '128.122.151.57'
DEBUG = True


def main():
	if USE_SSL:
		uri_type = "wss"
	else:
		uri_type = "ws"

	server_url = "%s://%s:%d/rpi/" % (uri_type, SERVER, PORT)

	if DEBUG:
		log.startLogging(sys.stdout)

	factory = ReconnectingWebSocketClientFactory(server_url, useragent = settings.RPI_USER_AGENT, debug = DEBUG)
	factory.protocol = RPIClientProtocol

	connectWS(factory)
	reactor.run()


if __name__ == '__main__':
	main()
