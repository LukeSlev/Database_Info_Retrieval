import parse, buildIndexes, Queries
from subprocess import call

def deleteFiles():
    call("rm -f terms.txt",shell=True)
    call("rm -f recs.txt",shell=True)
    call("rm -f years.txt",shell=True)
    call("rm -f termsOut.txt",shell=True)
    call("rm -f recsOut.txt",shell=True)
    call("rm -f yearsOut.txt",shell=True)
    call("rm -f te.idx",shell=True)
    call("rm -f re.idx",shell=True)
    call("rm -f ye.idx",shell=True)


def main():
    deleteFiles()
    parse.main()
    buildIndexes.main()
    Queries.main()


if __name__=="__main__":
    main()
