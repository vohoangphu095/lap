from lib import logo
print(logo)
str_last = []

while True:
    name = input('input name of aucutioner: ')
    prices = int(input('prices for this stage'))
    str = {}
    str['name'] = name
    str['prices'] = prices
    print(str)
    str_last.append(str)
    endgame = input('Press Y to Exit or press a key to continue').upper()
    if endgame == "Y":
        break
maxprices = max(str_last,key=lambda x: x['prices'])

print(str_last)
print('nguoi dau gia cao nhat',maxprices)
