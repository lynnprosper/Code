line = "101;Johnny 'wave-boy' Uones;usa;8.32;Fish;21"
s = {}
(s['id'],s['name'],s['country'],s['average'],s['board'],s['age']) = line.split(";")
print('ID:  ' + s['id'])
