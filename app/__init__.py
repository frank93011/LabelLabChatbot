import os
import sys
import errno
from flask import Flask
from linebot import LineBotApi, WebhookHandler
from werkzeug.middleware.proxy_fix import ProxyFix

app = Flask(__name__)
app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1, x_proto=1)
static_tmp_path = os.path.join(os.path.dirname(__file__), 'static', 'tmp')

# get channel_secret and channel_access_token from your environment variable
channel_secret = os.getenv('CHANNEL_SECRET', None)
channel_access_token = os.getenv('CHANNEL_ACCESS_TOKEN', None)
APIUrl = "https://labellab-backend.herokuapp.com/"
if channel_secret is None or channel_access_token is None:
    print('Specify CHANNEL_SECRET and CHANNEL_ACCESS_TOKEN as environment variables.')
    sys.exit(1)

line_bot_api = LineBotApi(channel_access_token)
handler = WebhookHandler(channel_secret)

from app import routes, models