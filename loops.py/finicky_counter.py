#Finicky Counter
#Demonstrate the break and conntinue statement
count=0
while True:
    count+=1
    #end loop if count greater than 10
    if count>10:
        break
    #skip 5
    if count==5:
        continue
    print("count")
