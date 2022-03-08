import json


def chestTesterGilded():
    lightPoolStart = '----------------------------------' + '\n' + 'Light Pool: ' + 2 * '\n'
    bonusPoolStart = '----------------------------------' + '\n' + 'Bonus pool: ' + 2 * '\n'

    g.write(bonusPoolStart)
    for i in data["pools"][0]["entries"]:
        try:
            g.write(i["_name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')
        except KeyError:
            g.write(i["name"] + '\n' + 'weight: ' + str(i['weight']) + 2 * '\n')

    g.write(lightPoolStart)

    for j in data['pools'][1]['entries']:
        try:
            g.write(j["_name"] + '\n' + 'weight: ' + str(j['weight']) + 2 * '\n') or g.write(j['name'])
        except KeyError:
            g.write(j["name"] + '\n' + 'weight: ' + str(j['weight']) + 2 * '\n') or g.write(j['name'])



def chestTesterNormal():
    trashPoolStart = '----------------------------------' + '\n' + 'Trash Pool: ' + 2 * '\n'
    resourcesPoolStart = '----------------------------------' + '\n' + 'Resources Pool: ' + 2 * '\n'
    powerupsPoolStart = '----------------------------------' + '\n' + 'Powerups Pool: ' + 2 * '\n'
    specialsPoolStart = '----------------------------------' + '\n' + 'Specials Pool: ' + 2 * '\n'

    g.write(trashPoolStart)
    for k in data["pools"][0]["entries"]:
        try:
            g.write(k["_name"] + '\n' + 'weight: ' + str(k['weight']) + 2 * '\n')
        except KeyError:
            g.write(k["name"] + '\n' + 'weight: ' + str(k['weight']) + 2 * '\n')

    g.write(resourcesPoolStart)
    for c in data["pools"][1]["entries"]:
        try:
            g.write(c["name"] + '\n' + 'weight: ' + str(c['weight']) + 2 * '\n')
        except KeyError:
            g.write(c["type"] + '\n' + 'weight: ' + str(c['weight']) + 2 * '\n')

    g.write(powerupsPoolStart)
    for w in data["pools"][2]["entries"]:
        try:
            g.write(w["name"] + '\n' + 'weight: ' + str(w['weight']) + 2 * '\n')
        except KeyError:
            g.write(w["type"] + '\n' + 'weight: ' + str(w['weight']) + 2 * '\n')

    try:
        g.write(specialsPoolStart)
        for e in data["pools"][3]["entries"]:
            try:
                g.write(e["name"] + '\n' + 'weight: ' + str(e['weight']) + 2 * '\n')
            except KeyError:
                g.write(e["type"] + '\n' + 'weight: ' + str(e['weight']) + 2 * '\n')
    except IndexError:
        pass


levels = [0, 25, 50, 75, 100, 150, 200, 250]
chType = ['gilded', 'normal']
rarities = ['common', 'rare', 'epic', 'omega']

print('Options:', chType)
chestType = input('Select chest type: ')  # 'normal'
print('Options:', rarities)
rarity = input('Select chest rarity: ')  # 'common'
print('Options:', levels)
lvl = input('Select chest level:')  # 0

path = str(input('Input path to the_vault folder: '))
if chestType == 'normal':
    chestType = 'vaultchest'

with open(
        r'' + path + 'the_vault\loot_tables\chest\lvl' + str(lvl) + '/' + chestType + rarity + '.json') as f:
    data = json.load(f)

g = open(r'' + str(input('Input path to the txt file you want to save the file to: ')), 'w')
if chestType == 'gilded':
    print(chestType, rarity, lvl)
    chestTesterGilded()
    print('end')
else:
    print(chestType, rarity, lvl)
    chestTesterNormal()
    print('end')
g.close()
