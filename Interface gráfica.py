import PySimpleGUI as psg

def calcular_irpf(sl_bruto, dependentes):
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

    return sl_bruto, dependentes, sl_base, alíquota * 100, ir_devido, sl_liquido, alíquota_efetiva * 100
psg.theme('DarkBrown6')
def main():
    while True:
        layout = [
            [psg.Text('Informe o Salário:'), psg.Input(key='salario')],
            [psg.Text('Informe o número de dependentes:'), psg.Input(key='dependentes')],
            [psg.Button('Calcular'), psg.Button('Fechar')],
        ]

        janela = psg.Window('Calculadora de IRPF mensal', layout)

        evento, valores = janela.read()

        if evento == psg.WIN_CLOSED or evento == 'Fechar':
            break

        try:
            sl_bruto = float(valores['salario'])
            dependentes = int(valores['dependentes'])

            sl_bruto, dependentes, sl_base, alíquota, ir_devido, sl_liquido, alíquota_efetiva = calcular_irpf(sl_bruto, dependentes)

            psg.popup(
                f'Salário bruto -- R$ {sl_bruto:.2f}',
                f'Número de dependentes -- {dependentes}',
                f'Salário base -- R$ {sl_base:.2f}',
                f'Alíquota -- {alíquota:.2f} %',
                f'Imposto de renda devido -- {ir_devido:.2f}',
                f'Salário líquido -- {sl_liquido:.2f}',
                f'Alíquota efetiva -- {alíquota_efetiva:.2f} %'
            )

        except ValueError:
            psg.popup_error('Informe valores válidos para salário e número de dependentes.')

        janela.close()

if __name__ == '__main__':
    main()
