from time import  sleep

# Nome aplicação.
print('CONTROLE DE ABASTECIMENTO VEICULAR')
print(' ')

# O que pretende fazer.
print('Dados de abastecimento ou trocar o óleo? ')

# Menu com duas opções.
print('[ 1 ] ABASTECIMENTO \n[ 2 ] TROCA DE ÓLEO \n[ 3 ] FINALIZAR ')
opção = int(input('Digite a opção desejada: '))

while opção != 3:

# Se for dados de abastecimento...
    if opção == 1:
        print('Certo, vamos lá...!')
        sleep(0.6)
        km_inic = float(input('Informe o km atual: '))
        km_final = float(input('Informe o km inicial: '))
        qtde_comb = float(input('Informe a quantidade de combustivél: '))
        print('Seu veicúlo está fazendo {:.3f} kms por litro.'.format((km_inic-km_final)/qtde_comb))

# Se for troca de óleo...
    if opção == 2:
        print('Certo, vamos lá...!')
        sleep(0.6)
        km_inic = float(input('Informe o km inicial: '))
        km_final = float(input('Informe o km final: '))
        print('Você rodou {} com o ultimo óleo trocado.'.format(km_inic-km_final))

# Caso a opção for finalizar.
    if opção == 3:
        print('Finalizando...')
        sleep(1)

# Caso digite uma opção inválida...
    else:
        print('Não há a opção \033[0:31m{}\033[m no menu. Tente novamente!'.format(opção))

print('Obrigado por utilizar nossos serviços!')

