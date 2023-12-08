# Calculadora de IRPF mensal
while True:
    # Apresentação

    print('\n\t\t\t -- Calculadora de IRPF mensal --\n')

    # Entradas

    sl_bruto = float(input('Informe o Salário: '))
    dependentes = int(input('informe o número de dependentes: '))

    # Processamento
    desc_dp = 189.59 * dependentes
    sl_base = sl_bruto - desc_dp

    if sl_base < 1903.98:
        alíquota = 0.0
        fx_desc = 0.0
        imp_bruto = (sl_base * alíquota) - fx_desc
    elif sl_base <= 2826.65:
        alíquota = 0.075
        fx_desc = 142.80
        imp_bruto = (sl_base * alíquota) - fx_desc
    elif sl_base <= 3751.05:
        alíquota = 0.15
        fx_desc = 354.80
        imp_bruto = (sl_base * alíquota) - fx_desc
    elif sl_base <= 4664.68:
        alíquota = 0.225
        fx_desc = 636.13
        imp_bruto = (sl_base * alíquota) - fx_desc
    else:
        alíquota = 0.275
        fx_desc = 869.36
        imp_bruto = (sl_base * alíquota) - fx_desc

    ir_devido = imp_bruto
    sl_liquido = sl_bruto - ir_devido
    alíquota_efetiva = ir_devido / sl_bruto

    print('\n\t -- Saída de dados -- \n')

    # Saida
    print('Salário bruto -- R$ {:.2f}'.format(sl_bruto))
    print('Número de dependentes -- {}'.format(dependentes))
    print('Salário base -- R$ {:.2f}'.format(sl_base))
    print('Alíquota -- {:.2f} %'.format(alíquota * 100))
    print('Imposto de renda devido -- {:.2f}'.format(ir_devido))
    print('Salário líquido -- {:.2f}'.format(sl_liquido))
    print('Alíquota efetiva -- {:.2f} %'.format(alíquota_efetiva * 100))

    print('\n ---- Selecione a opção desejada ----')

    print('1. Calcular outro Imposto de renda: ')
    print('2. Fechar: ')

    op = int(input(''))

    if op == 1:
        print('Carregando...')
    elif op == 2:
        print('Finalizado.')
        break
    else:
        print('Opção inválida')
        break
