'''
Find missing number from list
'''

lst = list(range(1,101))
lst.remove(29)

print(lst)

miss_num = sum(range(max(lst) + 1)) - sum(lst)
print(miss_num)