import glob

def get_matrix(directory):
    lst, table = [], []
    files = glob.glob('{}*.csv'.format(directory))
    for file in files:
        f = open(file, "r")
        lst += f.readlines()[1:]
    for line in lst:
        table.append(line.split(','))
    return table

def get_dict(matr):
    dct = {}
    for line in matr:
        dct[line[0]] = 0
    return dct
