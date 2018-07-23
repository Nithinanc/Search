from os import walk
match=input("Enter Exact Match string: ");
def readFile(filename):
    f=open(filename,'r', errors='ignore')
    content=f.read()
    if content.find(match)!=-1:
        print(filename)

def listFloders(mypath):
    #print(mypath)
    f=[]
    di=[]
    ##print("here")
    for (dirpath, dirnames, filenames) in walk(mypath):
        f.extend(filenames)
        ##print(f)
        di.extend(dirnames)
        break
    #print(f)
    #print(di)
    for file in f:
        readFile(mypath+'/'+file)
    for dirname in di:
        if(dirname=="pdms903"):
            continue
        listFloders(mypath+'/'+dirname)
        #print("Finished Search"+mypath+'/'+dirname)
listFloders("Z:/pdms009")
