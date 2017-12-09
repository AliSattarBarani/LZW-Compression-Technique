count = 255
conc = ""

L1 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z' ]

myInput = input("Enter Any String")
inpLen = len(myInput)

print()

print("The new entries in the dictionary are:")
for i in range(inpLen - 1):
   List_Length = len(L1)
   s = 0 
   for j in range(List_Length):
       if(myInput[i] == L1[j]):
           conc= myInput[i] + myInput[i + 1]
           for m in range(List_Length):
               if (conc == L1[m]):
                   s = s + 1
                   conc = conc + myInput[s + i + 1] 
               if (m == (List_Length - 1)):
                  count+=1
                  print()
                  print(count,'-', conc)
                  L1.append(conc)
                  conc = ""
                       

   
