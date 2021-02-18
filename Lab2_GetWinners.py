def GetWinners(rating, table):
    scores = [12, 10, 8, 7, 6, 5, 4, 3, 2, 1]
    for i in range(1, len(table)+1):
        lst = [line[i] for line in table]
        sorted_lst = sorted(lst, reverse=True)
        for j in range((len(lst) if len(lst)<10 else 10)):
            ind = lst.index(sorted_lst[j])
            rating[ind] = (rating[ind][0], rating[ind][1]+scores[j])
