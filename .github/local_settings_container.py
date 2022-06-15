import os

if os.getenv('OAUTH_CONSUMER_KEY'):
	OAUTH_CONSUMER_KEY = os.getenv('OAUTH_CONSUMER_KEY')
if os.getenv('OAUTH_CONSUMER_SECRET'):
	OAUTH_CONSUMER_SECRET = os.getenv('OAUTH_CONSUMER_SECRET')
if os.getenv('SECRET_KEY'):
	SECRET_KEY = os.getenv('SECRET_KEY')
if os.getenv('API_HOST'):
	API_HOST = os.getenv('API_HOST')
if os.getenv('API_PORTAL'):
	API_PORTAL = os.getenv('API_PORTAL')
if os.getenv('ALLOWED_HOSTS'):
	ALLOWED_HOSTS = os.getenv('ALLOWED_HOSTS').split(',')


