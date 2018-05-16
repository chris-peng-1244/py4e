import sqlite3

conn = sqlite3.connect('emaildb.sqlite')
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')

cur.execute('''
CREATE TABLE Counts (org TEXT, count INTEGER)''')

fname = input('Enter file name: ')
if (len(fname) < 1): fname = 'mbox-short.txt'
fh = open(fname)
count = dict()
for line in fh:
    if not line.startswith('From: '): continue
    pieces = line.split()[1].split('@')
    org = pieces[1]
    count[org] = count.get(org, 0) + 1

for org in count:
    cur.execute('''INSERT INTO Counts (org, count)
    VALUES(?, ?)''', (org, count[org]))
    conn.commit()

# https://www.sqlite.org/lang_select.html
sqlstr = 'SELECT org, count FROM Counts ORDER BY count DESC LIMIT 10'

for row in cur.execute(sqlstr):
    print(str(row[0]), row[1])

cur.close()