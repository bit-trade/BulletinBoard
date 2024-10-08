import os
from dotenv import load_dotenv


load_dotenv()
django_key = os.environ.get('SECRET_KEY')
