#Solution(Python):
#Function to check if the input file exists or not
def fileExists(file):
    try:
        f = open(file,'r')
        f.close()
    except FileNotFoundError:
        return False
    return True
#Function to check the presence of any empty line
def isLineEmpty(line):
    return len(line.strip()) < 1
#Function to remove empty lines
def removeEmptyLines(file):
    lines = []
    if not fileExists(file):
        print ("{} does not exist ".format(file))
        return
    out = open(file,'r')
    lines = out.readlines()
    out.close()
    out = open(file,'w')
    t=[]
    for line in lines:
        if not isLineEmpty(line):
            t.append(line)
    out.writelines(t)
    out.close()
#Function that evaluates the expressions in the input file
def excelfunction(file):
    if not fileExists(file):
        print("{} does not exist ".format(file))
        return
    out = open(file, 'r')
    lines = out.readlines()
    totaltc = int(lines[0])
    i=0
    while totaltc>0:
        int(i)
        i+=1
        tc = lines[i]
        for j in lines[int(i)+1:int(i)+int(tc)+1]:
            print(j.split(" = ")[0]+" = "+str(int(eval(j.split(" = ")[1]))))
        int(i)
        i+=int(tc)
        totaltc-=1
        print()

if __name__=="__main__":
    fileName = 'input.txt'
    fileExists(fileName)
    removeEmptyLines(fileName)
    excelfunction(fileName)
