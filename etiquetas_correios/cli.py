def main():
    from argparse import ArgumentParser

    parser = ArgumentParser(description='Gerar etiquetas para postagem nos Correios através de um arquivo CSV.')
    parser.add_argument('arquivo_csv')
    parser.add_argument('-o', '--arquivo-output', help='Arquivo de output. O output sairá para stdout se não especificado.')
    parser.add_argument('-s', '--preencher-com-sigep', action='store_true',
                        help='Consultar CEP no SIGEP e preencher com os dados retornados.')
    parser.add_argument('-p', '--papel', default='pimaco6184',
                        help='Tipo de papel para impressão. Valores disponíveis: pimaco6184 (padrão).')

    args = parser.parse_args()


if __name__ == '__main__':
    main()
