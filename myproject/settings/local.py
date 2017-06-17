from .base import *
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '$m2n)yb2bhl0!=8ie+&ubn#b7496zk)bd$*)0t4ldeyoak0fzr'

DEBUG = env.bool('DJANGO_DEBUG', default=True)