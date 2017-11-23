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

def runPerl(inp, out):
    # Kind of unsafe apparently, may wanna look into alternatives
    call('perl break.pl < {0} > {1}'.format(inp,out), shell=True)
    #result = Popen(["perl","break.pl"], stdout=subprocess.PIPE , input=inpFile.encode('utf-8'))
    #result.stdout.decode('utf-8')

def readyDBInp():
    t = "terms.txt"
    y = "years.txt"
    r = "recs.txt"

    runPerl(t, 'termsOut.txt')
    runPerl(y, 'yearsOut.txt')
    runPerl(r, 'recsOut.txt')

def loadDB(typ, inp, db):
    call('db_load -T -t {0} -f {1} {2} '.format(typ,inp,db), shell=True)

def checkDB(inp):
    call('db_dump -p {0} -f test.txt '.format(inp), shell=True)

def indexes():
    # inputs
    t = "termsOut.txt"
    y = "yearsOut.txt"
    r = "recsOut.txt"
    # outputs
    to = "te.idx"
    yo = "ye.idx"
    ro = "re.idx"

    loadDB('btree', t, to)
    loadDB('btree', y, yo)
    loadDB('hash', r, ro)

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
    sortFiles()
    create_indexies()
    readyDBInp()
    indexes()
    #checkDB("re.idx")


if __name__ == '__main__':
    main()
