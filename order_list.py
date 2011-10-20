import app.gmail as gmail

from app.settings import *

def order_list():
    gmail.send(ezmlm_listname + "-list@" + ezmlm_domain)

def main():
    order_list()

if __name__ == "__main__":
    main()
