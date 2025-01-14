# EXERCÍCIO DE CONVERSÃO DE MEDIDAS 

metro = float(input('Insira a medida em metros: '))

km = metro * 0.001
hm = metro * 0.01
dam = metro * 0.1
m = metro * 1
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print('O metro {} corresponde às medidas:\n{} km\n{} hm\n{} dam\n{} m\n{} dm\n{} cm\n{} mm' .format(metro, km, hm, dam, m, dm, cm, mm))