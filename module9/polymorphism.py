list_example=len("hello world")
list_example1=len((1,3,5))
list_example2=len(234,234,234)

print(list_example)
print(list_example1)
print(list_example2)


sum_of_list=sum([1,2,3,4,5])
sum_of_tuple=sum((1,2,5,8,9))

print(sum_of_tuple)
print(sum_of_tuple)

def add(x,y):
    return (x+y)

def concatenate(x,y):
    return str(x) + str(y)

def operator(operation, x,y):
    return operation(x,y)

result_sum=operator(add,5,2)
result_con=operator(concatenate,"Hello", "erin")

print(result_sum)
print(result_con)