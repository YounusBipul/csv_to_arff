filename="test.csv"

f= open(filename, "r")
s= f.readline()
data={}
k= s.find(",")
while k!=-1:
    e=s[0:k]
    data[e]=[]
    s=s[k+1:len(s)]
    k= s.find(",")
s=s[0:len(s)-1]
data[s]=[]

inst=0
s= f.readline()
while(s != ""):
    inst+=1
    for key in data:
        k= s.find(",")
        e=s[0:k]
        if e not in data[key]:
            data[key].append(e)
        s=s[k+1:len(s)]
    s=f.readline()
f.close()
n_filename=filename[0:len(filename)-3]
n_filename=n_filename+"arff"
print (n_filename)
nf= open(n_filename,"w")
print ("@relation relation_name")
nf.write("@relation relation_name"+"\n\n")
for key in data:
    j=1
    l=len(data[key])
    if l>int(inst/3):
        p= "@attribute "+key+" numric"
        
    else:
        p= "@attribute "+key+" {"
        for i in data[key]:
            if j!=1:
                p= p+" "+i
            else:
                p=p+i
            if l!=j:
                p=p+","
            j=j+1
        p=p+"}"
        print (p)
    nf.write(p+"\n")
        
f= open(filename, "r")
s=f.readline()
print ("\n@data")
nf.write("\n@data\n")
while s!="":
    s=s[0:len(s)-1]
    print (s)
    nf.write(s+"\n")
    s=f.readline()
f.close()
nf.close()



