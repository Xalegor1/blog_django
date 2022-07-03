import string

ltrs = string.ascii_lowercase
nums = [i for i in range(10, 46)]
res = zip(nums, ltrs)
# print(list(ltrs))
for i in res:
    print(i)
# print(list(res))


