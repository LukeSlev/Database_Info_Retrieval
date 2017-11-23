from subprocess import call
from subprocess import Popen
from bsddb3 import db

def sortFiles():
    t = "terms.txt"
    y = "years.txt"
    r = "recs.txt"

    call('sort -u -o {0} {1}'.format(t,t), shell=True)
    call('sort -u -o {0} {1}'.format(y,y), shell=True)
    call('sort -u -o {0} {1}'.format(r,r), shell=True)

def main():
    sortFiles()



def create_indexies():
    database1=db.DB()
    database1.open("re.idx",None,db.DB_HASH,db.DB_CREATE)
    database1.close()

    database2=db.DB()
    database2.open("te.idx",None,db.DB_BTREE,db.DB_CREATE)
    database2.close()

    database3=db.DB()
    database3.open("ye.idx",None,db.DB_BTREE,db.DB_CREATE)
    database3.close()

def main():
    # sort()
    # create_indexies()
    Popen(["perl","break.pl"])


if __name__ == '__main__':
    main()
