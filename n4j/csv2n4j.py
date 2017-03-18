import md5

plantilla = "CREATE (i%s:Web {title:'%s'})\nCREATE(i%s)-[:PARENT {}]->(i%s)\n"

def hash(text):
     return str(md5.new(text).hexdigest())


f = open('res.csv', 'r')
a = f.read()
f.close()

f = open('res.n4j', 'w')
exists = []
for x in a.split('\n'):
     r = x.split(';')
     if r[0] in exists:
             print(r)
             continue
     try:
      exists.append(r[0])
      f.write(plantilla%(hash(r[1]), r[0], hash(r[1]), hash(r[2])))
     except:
     	 print(r)
f.close()
