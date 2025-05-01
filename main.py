"""def openOrSenior(data):
  return ["Senior" if age >= 55 and handicap >= 8 else "Open" for (age, handicap) in data]"""
def open_or_senior(data):
    my_list = []
    for i in data:
        print(f'{i[0]}: {i[1]}')
        if i[0] >= 55 and i[1] > 7 :
            my_list.append('Senior')
        else:
            my_list.append('Open')
    return my_list
input =  [(14, 10),  (54, 17), (70, 24), (24, 26),(54, 8), (48, 16)]
data = open_or_senior(input)
print(data)


