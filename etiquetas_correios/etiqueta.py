import re
from decimal import Decimal

import attr

from .endereco import Endereco


@attr.s
class Etiqueta(object):
    remetente = attr.ib(validator=attr.validators.instance_of(Endereco))
    destinatario = attr.ib(validator=attr.validators.instance_of(Endereco))
    codigo_do_servico = attr.ib(validator=attr.validators.instance_of(int))
    valor_declarado = attr.ib(default=Decimal(0), validator=attr.validators.instance_of(Decimal))

    def gerar_string_data_matrix(self):
        self.remetente.validar()
        self.destinatario.validar()

        data_matrix = []

        # cep destino
        data_matrix.append(self.destinatario.cep[:8])

        # complemento cep
        try:
            data_matrix.append('{:0>5}'.format(int(self.destinatario.numero))[:5])
        except ValueError:
            data_matrix.append('0' * 5)

        # cep origem
        data_matrix.append(self.remetente.cep[:8])

        # complemento cep
        try:
            data_matrix.append('{:0>5}'.format(int(self.remetente.numero))[:5])
        except ValueError:
            data_matrix.append('0' * 5)

        # validador cep destino
        soma_numeros_cep = sum([int(i) for i in self.destinatario.cep])
        data_matrix.append(str((((soma_numeros_cep // 10) + 1) * 10) - soma_numeros_cep))

        # idv
        data_matrix.append('0' * 2)

        # etiqueta
        data_matrix.append('0' * 13)

        # serviço valor declarado
        if self.valor_declarado > 0:
            data_matrix.append('19')
        else:
            data_matrix.append('00')

        # serviços adicionais
        data_matrix.append('0' * 10)

        # cartão de postagem
        data_matrix.append('0' * 10)

        # código de serviço
        data_matrix.append('{:0>5}'.format(self.codigo_do_servico)[:5])

        # agrupamento
        data_matrix.append('0' * 2)

        # numero logradouro
        try:
            data_matrix.append('{:0>5}'.format(int(self.destinatario.numero))[:5])
        except ValueError:
            data_matrix.append('0' * 5)

        # complemento logradouro
        data_matrix.append('{:<20}'.format(self.destinatario.complemento or '')[:20])

        # valor declarado
        data_matrix.append('{:0>5}'.format(abs(int(self.valor_declarado)))[:5])

        # telefone destinatário
        telefone_numeros = 0
        if self.destinatario.telefone is not None:
            telefone_numeros = re.sub(r'\D', '', self.destinatario.telefone)

        data_matrix.append('{:0>12}'.format(telefone_numeros)[:12])

        # latitude
        data_matrix.append('-00.000000')

        # longitude
        data_matrix.append('-00.000000')

        # pipe
        data_matrix.append('|')

        # campo livre
        data_matrix.append(' ' * 30)

        return ''.join(data_matrix)
