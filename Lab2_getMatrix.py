import glob

def get_matrix(directory):
    files_content, table = [], []
    files = glob.glob('{}*.csv'.format(directory))
    for file in files:
        if file=="res.csv": continue
        f = open(file, "r")
        files_content += f.readlines()[1:]
        f.close()
    for line in files_content:
        if line[0]=='''"''':
            i = line[1:].index('"')+2
            name = line[:i]
            normal_name=''
            for symb in name:
                if symb=='"' or symb==",": continue
                normal_name+=symb
            line = normal_name+line[i:]
        table.append(line.strip('\n').split(','))
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j].isdigit(): table[i][j] = int(table[i][j])
            elif table[i][j][:2]=="0x": table[i][j]=convert(table[i][j])
    return table


def convert(hex):
    dct = {'a':10,
          'b':11,
           'c':12,
           'd':13,
           'e':14,
           'f':15}
    nums = hex[2:]
    l = len(nums)-1
    dec = 0
    for n in nums:
        if n.isdigit():
            dec += int(n)*16**l
            l-=1
        elif n in dct.keys():
            dec+=int(dct[n])*16**l
            l-=1
        else: return 0
    return dec
