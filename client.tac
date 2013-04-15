# tac file is a pytho file that configure an application object in twisted
# and it assign this object to the top-level variable application

from twisted.application import service, internet

from rpi_ws.client_protocol import RPIClientProtocol, ReconnectingWebSocketClientFactory
from rpi_ws import settings


def getService():
	server_url = "ws://128.122.151.57:9000/rpi/" #maybe I should change this later
	factory = ReconnectingWebSocketClientFactory(server_url, useragent = settings.RPI_USER_AGENT, debug = False)
	factory.protocol = RPIClientProtocol
	return internet.TCPClient(factory.host, factory.port, factory)

# this is the core part of any tac file, the creation of the root-level application object
application = service.Application("PiIOClient")

# attach the serevice to its parent application
service = getService()
service.setServiceParent(application)