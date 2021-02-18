import glob

def get_matrix(directory):
    lst, table = [], []
    files = glob.glob('{}*.csv'.format(directory))
    for file in files:
        if file=="res.csv": continue
        f = open(file, "r")
        lst += f.readlines()[1:]
        f.close()
    for line in lst:
        table.append(line.strip('\n').split(','))
    for i in range(len(table)):
        for j in range(len(table[i])):
            if table[i][j].isdigit(): table[i][j] = int(table[i][j])
    return table
