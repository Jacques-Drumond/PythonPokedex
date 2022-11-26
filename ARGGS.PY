def sum_items(*args):
    summ = 0
    for x in args:
        summ += x
    print(summ)


listt = [1,2,3,4,5,6,99]

sum_items(*listt)