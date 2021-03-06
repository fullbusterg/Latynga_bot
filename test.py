global prssmall, prsbig


prssmall = dict([('а', "a"), ('ә', "a'"), ('б', 'b'), ('д', 'd'), ('е', 'e'), ('ф', 'f'), ('г', 'g'), ('ғ', "g'"),
            ('х', 'h'), ('һ', 'h'), ('і', "i"), ('и', "i'"), ('й', "i'"), ('ж', 'j'), ('к', 'k'), ('л', 'l'),
            ('м', 'm'), ('н', 'n'), ('ң', "n'"), ('о', 'o'), ('ө', "o'"), ('п', 'p'), ('р', 'r'), ('с', 's'),
            ('ш', "s'"), ('ч', "c'"), ('т', 't'), ('ұ', 'u'), ('ү', "u'"), ('в', 'v'), ('ы', 'y'), ('у', "y'"),
            ('з', 'z'), ('қ', 'q')
            ])

prsbig = dict([('А', "A"), ('Ә', "A'"), ('Б', 'B'), ('Д', 'D'), ('Е', 'E'), ('Ф', 'F'), ('Г', 'G'), ('Ғ', "G'"),
           ('Х', 'H'), ('Һ', 'H'), ('І', "I"), ('И', "I'"), ('Й', "I'"), ('Ж', 'J'), ('К', 'K'), ('Л', 'L'),
           ('М', 'M'), ('Н', 'N'), ('Ң', "N'"), ('О', 'O'), ('Ө', "O'"), ('П', 'P'), ('Р', 'R'), ('С', 'S'),
           ('Ш', "S'"), ('Ч', "C'"), ('Т', 'T'), ('Ұ', 'U'), ('Ү', "U'"), ('В', 'V'), ('Ы', 'Y'), ('У', "Y'"),
           ('З', 'Z'), ('Қ', 'Q')
          ])

def latinize(msg):
    global prsbig, prssmall
    nmsg = ""
    for ch in msg:
        if ch in prssmall:
            nmsg += prssmall[ch]
        elif ch in prsbig:
            nmsg += prsbig[ch]
        else:
           nmsg += ch
    return nmsg

def main() :
     print(latinize('е там өмір қалай бауырым, не жаңалық, Әлібөғңқ'))

if __name__ == '__main__':
    main()
