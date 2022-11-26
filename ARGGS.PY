def sum_items(*args):
    summ = 0
    for x in args:
        summ += x
    print(summ)


listt = [1,2,3,4,5,6,99]

sum_items(*listt)

def my_sum(*args):
    print(sum(args))

my_list = [1, 2, 3,45]
my_sum(*my_list)