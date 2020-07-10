import json
# a=open("write.json")
# data = json.load(a)
#
# print(data[3]['name'])
# a.close()
#
def read_data():
    with open("write.json") as file:
        return json.load(file)


def display(acc):
    data = read_data()
    if acc in data[0].keys():
        new_data = data[0][acc]
        print(new_data)
        for x in new_data:
            print("{}==>{}".format(x, new_data[x]))
    else:
        print('account does not exist')

def new_account():
    l = ['name', 'Age', 'Address', 'Balance']
    d = {}
    for x in l:
        if x == 'Age':
            y = int(input('Enter {} : '.format(x)))
            d[x]=y
        else:

            y = input('Enter {} : '.format(x))
            d[x] = y
    data = read_data()
    data = data[0]
    x = len(data)
    x = x+1
    x = str(x)
    x = {x: d}
    data.update(x)
    data = [data]
    f = open("write.json", 'w')
    json.dump(data, f)
    f.close()


new_account()

