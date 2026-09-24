with open("salary.txt", "r") as rf:
          with open("Output",'a') as wf:
               for line in rf.readlines():
                   name,salary=line.split(',')
                   wf.write(f'{name}\s salary is {salary}')
        
                
                          
                