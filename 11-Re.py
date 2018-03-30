import re

filename = input("Enter file name:")
h = open(filename)

print(sum([ int(num) for num in re.findall(r'\d+', h.read()) ]))
# total = 0
# for line in h:
#   nums = [ int(num) for num in re.findall(r'\d+', line) ]
#   total = total + sum(nums)

# print(total)
