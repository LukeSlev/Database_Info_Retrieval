import bsddb3
import re


def main():
    records = "(<\w+ key=\")([-\w\//]+)(\">)"  # Looks for the records key
    regex = re.compile('[^a-zA-Z0-9_ ]')  # valid characters in the text

    with open("long-test.txt", "r") as inp, open("terms.txt", "w") as terms, open("years.txt", "w") as years, \
            open("recs.txt", "w") as recs:
        for line in inp:

            l = [p.split('>') for p in line.split('<') if ('>' in p and '/' not in p)]
            if len(l) == 0:
                continue
            elif l[-1][0] == 'dblp':
                continue
            else:
                key = re.findall(records, line)[0][1]
                recs.write(key + ':' + line)

                for tok in l:
                    tok[1] = regex.sub(' ', tok[1])
                    if tok[0] == 'year':
                        years.write(tok[1] + ':' + key + '\n')
                    elif tok[0] == 'author':
                        for rest in tok[1].split():
                            if len(rest) > 2 and not rest.isdigit():
                                rest = re.sub(regex, ' ', rest)
                                terms.write('a-' + rest.lower() + ':' + key + '\n')
                    elif tok[0] == 'title':
                        for rest in tok[1].split():
                            if len(rest) > 2 and not rest.isdigit():
                                rest = re.sub(regex, ' ', rest)
                                terms.write('t-' + rest.lower() + ':' + key + '\n')
                    else:
                        for rest in tok[1].split():
                            if len(rest) > 2 and not rest.isdigit():
                                rest = re.sub(regex, ' ', rest)
                                terms.write('o-' + rest.lower() + ':' + key + '\n')




            # print(l)
            # print(line)




if __name__ == '__main__':
    main()
