import os
DATABASE = os.getenv('POSTGRES_DATABASE','postgres')
USER = os.getenv('POSTGRES_USER','postgres')
HOST = os.getenv('POSTGRES_HOST','db')


