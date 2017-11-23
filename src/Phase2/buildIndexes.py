from subprocess import call

def main():
    t = "terms.txt"
    y = "years.txt"
    r = "recs.txt"

    call('sort -u -o {0} {1}'.format(t,t), shell=True)
    call('sort -u -o {0} {1}'.format(y,y), shell=True)
    call('sort -u -o {0} {1}'.format(r,r), shell=True)


if __name__ == '__main__':
    main()