horas = int(input('Digite o número de horas extras que você tem: '))
horasfalt = int(input('Digite o número de horas que você faltou: '))
if horas > (horasfalt * 1.5):
    print ('Você ganhará 500 reais a mais')
else:
    print('Vai trabalhar mais vagabundo.')