import re

filename = input("Enter file name:")
h = open(filename)

nums = [ int(num) for num in re.findall(r'\d+', h.read()) ]
print(sum(nums))
