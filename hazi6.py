file = open("hazi.txt", "r",encoding='UTF-8')
tartalom = file.readlines()

for sor in tartalom:
    sor = sor.rstrip()
    print(sor)
for sor in tartalom:
    nelkuli = sor.lower().replace(',', '').replace('.', '').replace('?','').replace('!','').replace('-','');

with open("kihazi.txt", "w") as fp:
    for sor in tartalom:
        if not sor.isspace():
            fp.write(sor)



file.close()




