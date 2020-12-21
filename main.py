"""Arquivo principal que será interpretado pelo interpretador."""


def main():
    """Função principal que será rodada quando o script for passado para o interpretador."""
    # COLOQUE SEU CÓDIGO AQUI
    número_1 = float(input('Digite o primeiro número: \n'))
    número_2 = float(input('Digite o segundo número: \n'))
    número_3 = float(input('Digite o terceiro número: \n'))

    if número_1 >= número_2 and número_1 >= número_3:
      maior = número_1
    elif número_2 >= número_1 and número_2 >= número_3:
      maior = número_2
    else:
      maior = número_3

    print(f'{maior}')


if __name__ == '__main__':
    main()
