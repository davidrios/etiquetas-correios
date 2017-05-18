import re

import attr

from .exc import ErroEnderecoInvalido


_ENDERECO_CAMPOS_NONE = {'nome2', 'complemento', 'telefone'}


@attr.s
class Endereco(object):
    nome1 = attr.ib(validator=attr.validators.instance_of(str))
    cep = attr.ib()
    numero = attr.ib(validator=attr.validators.instance_of(int))
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

    def validar(self):
        erros = []

        try:
            self._valida_cep('cep', self.cep)
        except Exception as ex:
            erros.append(str(ex))

        if not isinstance(self.numero, int):
            erros.append('Número inválido')

        for atributo in ('nome1', 'nome2', 'endereco', 'complemento', 'bairro', 'cidade', 'uf', 'telefone'):
            atributo_valor = getattr(self, atributo)

            if not (isinstance(atributo_valor, str) or (atributo in _ENDERECO_CAMPOS_NONE and atributo_valor is None)):
                erros.append('{} deve ser uma str'.format(atributo))

        if erros:
            raise ErroEnderecoInvalido(erros)
