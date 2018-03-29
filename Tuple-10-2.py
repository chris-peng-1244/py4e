name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

freq = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    time = line.split()[5].split(':')
    hour = time[0]
    freq[hour] = freq.get(hour, 0) + 1

freqItems = list(freq.items())
freqItems.sort()
for h, v in freqItems:
    print(h, v)
