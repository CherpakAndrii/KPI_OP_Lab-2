def rating(rating):
    res = open("res.csv", "w")
    rating.sort(key=itemgetter(1))
    for pair in rating[:10]:
        res.write(pair[0]+','+str(pair[1])+"\n")
    res.close()
