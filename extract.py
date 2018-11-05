from itertools import islice
import csv
DrugU = {}
file = open('data/Drug_Utilization_2011_-_All_States.csv','r')
reader = csv.reader(file)
for i,row in enumerate(reader):
    if i==0:
        continue
    key = row[1]
    value = row[11].replace(',','')
    value2 = row[12].replace(',','')
    value3 = row[13].replace(',','')
    if value !='':
        value = float(value)
    else:
        value = 0

    if value2 !='':
        value2 = float(value2)
    else:
        value2 = 0

    if value3 !='':
        value3 = float(value3)
    else:
        value3 = 0

    if key in DrugU:
        DrugU[key][0] += value
        DrugU[key][1] += value2
        DrugU[key][2] += value3
        #print DrugU
    else:
        DrugU[key] = [value,value2,value3]
        #print DrugU

print "done!"
#print DrugU\
temp1 = 0
temp2 = 0
for key in DrugU:
    temp1 +=DrugU[key][0]
    temp2 +=DrugU[key][1]

print temp1
print temp2
keys = sorted(DrugU.keys())
print keys

txtName = "DrugU2009_total.txt"
f=open(txtName, "a")
for key in keys:
    print key
    print DrugU[key]
    temp = "{name:'"+key+"',value:"+str(DrugU[key][0])+"},\n"
    #temp = key+":"+str(DrugU[key][0])+','+str(DrugU[key][1])+','+str(DrugU[key][2])+"\n"
    f.write(temp)
f.close()
txtName = "DrugU2009_medicaid.txt"
f1=open(txtName, "a")
for key in keys:
    print key
    print DrugU[key]
    temp = "{name:'"+key+"',value:"+str(DrugU[key][1])+"},\n"
    #temp = key+":"+str(DrugU[key][0])+','+str(DrugU[key][1])+','+str(DrugU[key][2])+"\n"
    f1.write(temp)
f1.close()

txtName = "DrugU2009_nonmedicaid.txt"
f2=open(txtName, "a")
for key in keys:
    print key
    print DrugU[key]
    temp = "{name:'"+key+"',value:"+str(DrugU[key][2])+"},\n"
    #temp = key+":"+str(DrugU[key][0])+','+str(DrugU[key][1])+','+str(DrugU[key][2])+"\n"
    f2.write(temp)
f2.close()