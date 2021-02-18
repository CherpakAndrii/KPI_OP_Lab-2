from Lab2_getMatrix import get_matrix
from Lab2_Outp import outp

dir = input("Enter the directory: ")
table = get_matrix(dir)
rating = [(l[0], 0) for l in table]
