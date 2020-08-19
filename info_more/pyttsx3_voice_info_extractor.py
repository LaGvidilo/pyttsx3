import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
liste_cols=['index','age', 'gender', 'id', 'languages', 'name']
f = open("out.csv","w")
f.write(",".join(liste_cols)+"\n")
index=0
for i in voices:
	f.write(str(index)+","+str(i.age)+","+str(i.gender)+","+str(i.id)+","+str(i.languages)+","+str(i.name)+"\n")
	index+=1
f.close()