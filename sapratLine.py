with open("C:\\THINGS\\githup project\\FULL BOT RESORSE\\surse.txt",'r',encoding='utf-8') as surse:
    with open("C:\\THINGS\\githup project\\FULL BOT RESORSE\\qus.txt",'w',encoding='utf-8') as f1:
        with open("C:\\THINGS\\githup project\\FULL BOT RESORSE\\ans.txt",'w',encoding='utf-8') as f2:
            for line in surse:

                word = line.split()

                if word[0] == " ":
                    f1.write(" ".join(word[1:]) + "\n")

                elif word[0] == "   ans  ":
                    f2.write(" ".join(word[1:]) + "\n")