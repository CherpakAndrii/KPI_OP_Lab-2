import glob

def get_matrix(directory):
    lst, table = [], []
    files = glob.glob('{}*.csv'.format(directory))
    for file in files:
        f = open(file, "r")
        lst += f.readlines()[1:]
        f.close()
    for line in lst:
        table.append(line.split(','))
    return table
