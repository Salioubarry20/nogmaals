dag = input('Zet hier welke dag (ma/di/woe/don/vrij/za/zo): ')
ma = 'maandag '
di = 'dinsdag '
woe = 'woensdag '
do = 'donderdag '
vrij = 'vrijdag '
za = 'zaterdag '
zo = 'zondag '

while dag == 'ma' or dag == 'maandag':
    print(ma)
    break
while dag == 'di' or dag == 'dinsdag':
    print(ma + di)
    break
while dag == 'woe' or dag == 'woensdag':
    print(ma + di + woe)
    break
while dag == 'do' or dag == 'donderdag':
    print(ma + di + woe + do)
    break
while dag == 'vrij' or dag == 'vrijdag':
    print(ma + di + woe + do + vrij)
    break
while dag == 'za' or dag == 'zaterdag':
    print(ma + di + woe + do + vrij + za)
    break
while dag == 'zo' or dag == 'zondag':
    print(ma + di + woe + do + vrij + za + zo)
    break