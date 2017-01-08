import bottle
import os
import sys
import ConfigParser

# routes contains the HTTP handlers for our server and must be imported.
import routes.root
import routes.temperature

try:
    os.system('modprobe w1-gpio')
    os.system('modprobe w1-therm')
except:
    print ('!!! no started raspberry 1-Wire configuration !!!')

def get_root_foolder():
    return os.path.abspath(os.path.dirname(__file__))

configParser = ConfigParser.RawConfigParser()
configFilePath = os.path.join(get_root_foolder(), 'config.ini')
configParser.read(configFilePath)

if '--debug' in sys.argv[1:] or 'SERVER_DEBUG' in os.environ:
    # Debug mode will enable more verbose output in the console window.
    # It must be set at the beginning of the script.
    print ("In Debug")
    bottle.debug(True)

if configParser.getboolean('Global', 'debug') :
    print 'Execution with remote debug'
    import ptvsd
    ptvsd.enable_attach(secret='pydebug')

def wsgi_app():
    """Returns the application to make available through wfastcgi. This is used
    when the site is published to Microsoft Azure."""
    return bottle.default_app()



if __name__ == '__main__':
    HOST = os.environ.get('SERVER_HOST', '0.0.0.0')
    try:
        PORT = int(os.environ.get('SERVER_PORT', configParser.get('Global', 'port')))
    except ValueError:
        PORT = 5555

    # Starts a local test server.
    bottle.run(server='wsgiref', host=HOST, port=PORT)
