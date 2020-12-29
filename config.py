
branch = 'main'


EXT_IP = '34.90.19.13'
INT_IP = '10.164.0.2'

tg_tokens = {
    'dev': '1042488699:AAFEsvgJXyEIR3REXrSAMZjQB-HClDnNE0U',
    'main': '1490631920:AAHCSpYQ_DjzqnbgpmcJiM2eZIBMLi-wSDk'
}
webhook_hosts = {
    'dev': 'localhost',
    'main': INT_IP
}
webhook_ports = {
    'dev': 80,
    'main': 8443
}
db_hosts = {
    'dev': EXT_IP,
    'main': 'localhost'
}
filter_hosts = {
    'dev': 'localhost',
    'main': INT_IP
}
filter_ports = {
    'dev': 82,
    'main': 8440
}

TOKEN = tg_tokens[branch]

WEBHOOK_LISTEN = webhook_hosts[branch]
WEBHOOK_PORT = webhook_ports[branch]

WEBHOOK_SSL_CERT = "/home/rent_b/ssl/ssl.pem"
WEBHOOK_SSL_PRIV = "/home/rent_b/ssl/ssl_priv.pem"

IMAGE_FOLDER = 'photos'
ADMIN_PASSWORD = 'admin'

DATA_UPDATE_TIME = 600 # sec
USER_DATA_UPDATE_TIME = 30 # sec
USER_DATA_OLD_TIME = 60 # sec

DB_USER = 'postgres'
DB_PASSWORD = 'SF899laxe_'
DB_DATABASE = 'rent'
DB_HOST = db_hosts[branch]

FILTER_APP_HOST = filter_hosts[branch]
FILTER_APP_PORT = filter_ports[branch]