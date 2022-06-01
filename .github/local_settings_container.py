import os


if 'OAUTH_CONSUMER_KEY' in os.environ:
	OAUTH_CONSUMER_KEY = os.environ['OAUTH_CONSUMER_KEY']
if 'OAUTH_CONSUMER_SECRET' in os.environ:
	OAUTH_CONSUMER_SECRET = os.environ['OAUTH_CONSUMER_SECRET']
if 'SECRET_KEY' in os.environ:
	SECRET_KEY = os.environ['SECRET_KEY']
if 'API_HOST' in os.environ:
	API_HOST = os.environ['API_HOST']
if 'API_PORTAL' in os.environ:
	API_PORTAL = os.environ['API_PORTAL']
if 'ALLOWED_HOSTS' in os.environ:
	ALLOWED_HOSTS = os.environ['ALLOWED_HOSTS'].split(',')
if 'VERIFY' in os.environ:
	VERIFY = os.environ['VERIFY']
