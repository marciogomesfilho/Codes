# Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de
# tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.


larg = float  (input('digite a largura da parede: '))
altu = float (input('digite a altura da parede: '))
area = larg*altu
print ('a área da parede é {}'.format(area))

tinta = area/2

print ('será necessário {}L de tinta para pintar'.format(tinta))


# a cada 2 metros quadrados de tinta pinta 2 metros quadrados

