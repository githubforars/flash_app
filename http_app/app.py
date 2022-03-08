#!env python3
from flask import Flask, request
import logging
from argparse import *

log = logging.getLogger('werkzeug')
logging.basicConfig(level=logging.ERROR,format='%(asctime)s  Request-URI: %(message)s')
log.setLevel(logging.ERROR)

### arg_parser  ###
def arg_parser():
    parser = ArgumentParser()
    parser.add_argument('-d', '--debug', help='debug flag',action='store_true',required=False)
    args = parser.parse_args()
    global flag
    if args.debug:
       flag=True
    else:
       flag=False


def init_app():
  app = Flask(__name__)
  @app.route('/', defaults={'path': ''},methods=['GET','POST'])
  def echo(path):
    if request.method == 'GET' and request.headers.get('Accept') == 'application/json':
        app.logger.debug(request.path)
        return({"message": "Hello, World"})
    else:
        app.logger.debug(request.path)
        return('<p>Hello, World</p>')
  return app

if __name__ == '__main__':
    arg_parser()
    app = init_app()
    app.run(debug=flag, host='0.0.0.0', port=5000)
