with open('zeugnis_beispiel.txt', 'r') as f: content = f.read()
with open('zeugnissprache.csv', 'r') as f: code = f.read()

for exp in code.split('\n'):
    exp = exp.split(';')
    if exp[1] in content: print 'Bewertung', exp[2], 'in Kategorie', exp[0]
