import os,sys

BASE_PATH = os.path.dirname(os.path.dirname((os.path.abspath(__file__))))
sys.path.append(BASE_PATH)
from core import main

if __name__ == '__main__':
    main.ArgvHandle()