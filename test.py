import functions as nem

login = nem.login("bfulham@bradyfulham.com", "paSnoq-hiqco8-ducjuf")

home = nem.meter(20021737816, login)
print(home.getdata("D:\\Users\\Bfulh\\Desktop\\sapn meterdata\\data"))