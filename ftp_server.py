from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

# Define a directory to save the uploaded images
image_directory = "./"

# Set up a dummy authorizer with a user and password
authorizer = DummyAuthorizer()
authorizer.add_user("user", "password", image_directory, perm="elradfmw")

# Set up the FTP handler
handler = FTPHandler
handler.authorizer = authorizer

# Define the FTP server and bind it to a port
server = FTPServer(("0.0.0.0", 26), handler)

# Start the FTP server
server.serve_forever()
