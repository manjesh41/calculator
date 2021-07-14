def myFunction(textxtring):
    listOfLines=textstring.split('\n')
    for line in listOfLines:
         s=len(line)
         for i in range(len(line)):
             if line[i]=='#':
                 s=i
                 break
        print(line[0:5])
myFunction('d=4\nt=2 \ns=d/t #speed')
