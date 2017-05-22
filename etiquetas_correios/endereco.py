import re

import attr

from .exc import ErroEnderecoInvalido


_ENDERECO_CAMPOS_NONE = {'nome2', 'complemento', 'telefone'}

_UFS_BRASIL = {
    'AC',
    'AL',
    'AM',
    'AP',
    'BA',
    'CE',
    'DF',
    'ES',
    'GO',
    'MA',
    'MG',
    'MS',
    'MT',
    'PA',
    'PB',
    'PE',
    'PI',
    'PR',
    'RJ',
    'RN',
    'RO',
    'RR',
    'RS',
    'SC',
    'SE',
    'SP',
    'TO',
}


@attr.s
class Endereco(object):
    nome1 = attr.ib(validator=attr.validators.instance_of(str))
    cep = attr.ib()
    numero = attr.ib(validator=attr.validators.instance_of(str))
    endereco = attr.ib(default=None)
    complemento = attr.ib(default=None)
    bairro = attr.ib(default=None)
    cidade = attr.ib(default=None)
    uf = attr.ib(default=None)
    telefone = attr.ib(default=None)
    nome2 = attr.ib(default=None)

    @cep.validator
    def _valida_cep(self, atributo, valor):
        if valor is None or re.match(r'^\d{8}$', valor) is None:
            raise ValueError('CEP inválido')

    @property
    def endereco_numero(self):
        return '{}, {}'.format(self.endereco, self.numero)

    @property
    def cep_formatado(self):
        return '{}-{}'.format(self.cep[:5], self.cep[5:])

    def validar(self):
        erros = []

        try:
            self._valida_cep('cep', self.cep)
        except Exception as ex:
            erros.append(str(ex))

        for atributo in ('nome1', 'nome2', 'numero', 'endereco', 'complemento', 'bairro', 'cidade', 'uf', 'telefone'):
            atributo_valor = getattr(self, atributo)

            if not (isinstance(atributo_valor, str) or (atributo in _ENDERECO_CAMPOS_NONE and atributo_valor is None)):
                erros.append('{} deve ser uma str'.format(atributo))

        if self.uf not in _UFS_BRASIL:
            erros.append('UF inválida')

        if erros:
            raise ErroEnderecoInvalido(erros)
