from subprocess import call
from subprocess import Popen
from bsddb3 import db

def sort():
    t = "terms.txt"
    y = "years.txt"
    r = "recs.txt"

    call('sort -u -o {0} {1}'.format(t,t), shell=True)
    call('sort -u -o {0} {1}'.format(y,y), shell=True)
    call('sort -u -o {0} {1}'.format(r,r), shell=True)


def create_indexies():
    database=db.DB()
    database.open("re.idx",None,db.DB_HASH,db.DB_CREATE)
    database.close()

    database=db.DB()
    database.open("te.idx",None,db.DB_BTREE,db.DB_CREATE)
    database.close()

    database=db.DB()
    database.open("ye.idx",None,db.DB_BTREE,db.DB_CREATE)
    database.close()

def main():
    # sort()
    # create_indexies()
    Popen(["perl","break.pl"])


if __name__ == '__main__':
    main()
