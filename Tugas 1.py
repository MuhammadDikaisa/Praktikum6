telepon = {
    'Muhammad' : '081384245435',
    'Dikaisa' : '082122990441'
}

print(telepon['Muhammad'])

print("\n")
telepon['Alberttt'] = '087654544'
telepon['Dikaisa'] = '088999776'

print(telepon.keys())
print(telepon.values())

print("\n")

print("Nama\t| Nomor Telepon ")
print("======================")

for nama,nomor in telepon.items():
    print("%s \t| %s " % (nama,nomor))

print("\n")

del telepon['Dikaisa']
print("Nama\t| Nomor Telepon")
print("======================")
for key,val in telepon.items():
    print("%s \t| %s " % (key,val))