def similarity(high, low):
    correct = 0
    for i in low:
        i = int(i)
        for j in high:
            j = int(j)
            if i == j:
                correct += 1
    return correct


def iterate_clusters(redued_list, high_list):
    reduced_sim = []
    best = []
    for t in range(len(reduced_list)):
        a=0
        print('reduced cluster: '+str(t))
        for h in range(len(high_list)):
            if h not in best:
                sim = similarity(high_list[h], reduced_list[t])
                if  sim > a:
                    a = sim
                    top = h
        best.append(top)
        print('high cluster: '+str(top))
        reduced_sim.append(a) 
    return reduced_sim


def print_similarty_percentage(reduced_sim):
    tot = 0
    for y in reduced_sim:
        print('The number of similar points is: ' +str(y))
        tot += y
        print('The total number of similar points is (so far):' +str(tot))
    print('The total number of similar points is (so far):' +str(tot))
    tot =(tot/len(reduced))*100
    print(tot)
