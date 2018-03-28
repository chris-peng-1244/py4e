name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

emails = dict()
for line in handle:
    if not line.startswith('From '):
        continue
    words = line.rstrip().split()
    emails[words[1]] = emails.get(words[1], 0) + 1

maxCount = None
bestEmail = None
for k,v in emails.items():
    if maxCount is None or v > maxCount:
        maxCount = v
        bestEmail = k

print(bestEmail, maxCount)