import xmltodict

with open("movies.xml",'rb') as f:
    data = xmltodict.parse(f)
data = data['collection']
for x in data:
    if x == '@shelf':
        print("Root element : {}".format(data['@shelf']))
    else:
        for d in data[x]:
            print("*****Movie*****")
            for k in d:
                if k == "@title":
                    print("{} : {}".format(k[1:].capitalize(), d[k]))
                else:
                    print("{} : {}".format(k.capitalize(), d[k]))

