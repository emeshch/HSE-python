import re
file = open("phones.txt", "r+")                   
text = file.read()
#match = re.findall(r'', text)
nominus = re.sub(r'-', "", text)
match = re.findall(r'\t\+?7\D?(\d{3})\D?.{7}|\t8(\d{3}).{7}|\t(\d{3}).{7}', nominus)
#file.write(rr)
codelist = []
for i in match:
    for k in i:
        if len(k) > 1:
            codelist.append(k)
freq = {num: codelist.count(num) for num in codelist}
print(freq)
file.close
