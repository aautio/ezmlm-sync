import app.gmail as gmail

from app.settings import ezmlm_listnames
from app.settings import ezmlm_domain

def order_lists():
	for listname in ezmlm_listnames:
	    gmail.send(listname + "-list@" + ezmlm_domain)

def main():
    order_lists()

if __name__ == "__main__":
    main()
