import io

myFile = open('C:\\Users\\1021053\\Documents\\script.txt', 'r', encoding='utf_16')
dan = myFile.readlines()
f = open("demofile3.txt", "a", encoding='utf_16')
for line in dan:
        line = line.strip()
        line = line.replace('\'', '\'\'')
        newLine  = "select '" + line + "' from dual;"
        print(newLine)
        f.writelines(newLine + '\n')

myFile.close()
f.close()
