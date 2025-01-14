# PROPORÇÃO DE PAREDE E QUANTIDADE DE TINTA NECESSÁRIA

largura = float(input('Insira a largura da parede em metros: '))
altura = float(input('Insira a altura da parede em metros: '))

área = largura * altura
quant_tinta = área / 2

print('Para uma área de {}m², são necessários {} litros de tinta.'.format(área, quant_tinta))