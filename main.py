import requests

def main():
    #RECEBE O CEP A SER CONSULTADO, ESSE VALOR RECEBIDO VAI SER UTILIZADO NA URL DE CONEXÃO DO WEBSERVICE QUE ESTÁ MAIS ABAIXO DO CÓDIGO
    cep = input('Digite o CEP a ser consultado: ')

    #VERIFICA SE O VALOR PASSADO ESTÁ EM NÚMEROS INTEIROS
    if cep.isnumeric() == False:
        print('CEP INVÁLIDO, DIGITE SOMENTE NÚMEROS\n')
        main()
    #VERIFICA SE O VALOR PASSADO POSSUI 8 DÍGITOS(QUANTIDADE DE DÍGITOS PADRÃO DE CEP)  
    elif len(cep) != 8:
        print('\nQuantidade de dígitos incorreta, o CEP deve conter 8 dígitos.\n')
        main()

    #CONEXÃO COM WEBSERVICE
    r = requests.get(f'https://viacep.com.br/ws/{cep}/json/')

    #EXIBIR RESULTADOS ENCONTRADOS
    print('=================')
    print('CEP ENCONTRADO')
    print('=================')
    print()

    print('CEP:', r.json()['cep'])
    print('Logradouro:', r.json()["logradouro"])
    print('Bairro:', r.json()["bairro"])
    print(f'Localidade: {r.json()["localidade"]}, {r.json()["uf"]}')
    print('Código IBGE:', r.json()["ibge"])

    #VERIFICA SE O USUÁRIO DESEJA CONTINUAR A UTILIZAR O SISTEMA OU DESEJA SAIR.
    #ENQUANTO O USUÁRIO NÃO DIGITAR UM VALOR VÁLIDO, O SISTEMA CONTINUA EM LOOPING ATÉ RECEBER UM VALOR VÁLIDO.
    continua = input('\n1. Faça outra consulta \n2. Sair\n')
    verifica = False
    while verifica == False:
        if continua.isnumeric() == False:
            print('\nOpção inválida')
            continua = input('\n1. Faça outra consulta \n2. Sair\n')
        if continua != '1' and continua != '2':
            print('\nOpção inválida')
            continua = input('\n1. Faça outra consulta \n2. Sair\n')
        if continua == '1':
            main()
        if continua == '2':
            print('Volte sempre!')
            verifica = True
            exit()
    

if __name__ == '__main__':
    main()