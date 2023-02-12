import re


rmnum = re.compile(r'/d+')
one = []

with open("C:\\THINGS\\githup project\\meshochat.txt", 'r', encoding= "utf-8") as mesho:
    for line in mesho:
        rm = line.replace('/','').replace(':','').replace('AM','').replace('PM','').replace('-','').replace(',','').replace(' ','').replace('ميشووو','ques ').replace('Nõr','ans ')
        one.append(rm)


        

with open("C:\\THINGS\\githup project\\res.txt",'w',encoding='utf-8') as reslut:
    for line in one:
        reslut.write(line)