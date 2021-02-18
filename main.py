from Lab2_getMatrix import get_matrix
from Lab2_Outp import outp
from aaaaa import GetWinners

directory = input("Enter the directory: ")
if directory == None: directory = "C:\\Users\\User\Desktop\Навчання\ОП\Lab_2\\"
table = get_matrix(directory)
rating = [(l[0], 0) for l in table]     #I'm using array generator, don't warry 'bout)
GetWinners(rating, table)
outp(rating)
