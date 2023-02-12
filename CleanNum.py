import re 

rmnum = re.compile(r'\d+')

with open("C:\\THINGS\\githup project\\res.txt",'r',encoding='utf-8') as line:
    time = line.read()

nonum = re.sub(rmnum, '', time)


with open("C:\\THINGS\\githup project\\res.txt",'w',encoding='utf-8') as line:

    line.write(nonum)



