try:
    from zeep import Client
except ImportError:
    raise Exception('Para usar a consulta SIGEP você deve instalar a dependência adicional [sigep].')


_URL_SIGEP = 'https://apps.correios.com.br/SigepMasterJPA/AtendeClienteService/AtendeCliente?wsdl'

_cliente_sigep = None


def _get_cliente_sigep():
    global _cliente_sigep
    if _cliente_sigep is None:
        _cliente_sigep = Client(_URL_SIGEP)

    return _cliente_sigep


def preencher_com_sigep(endereco):
    sigep = _get_cliente_sigep()

    resultado = sigep.service.consultaCEP(endereco.cep)
    resultado['endereco'] = resultado['end']

    for atributo in ('endereco', 'bairro', 'cidade', 'uf'):
        valor = resultado[atributo]
        if valor is None:
            continue

        setattr(endereco, atributo, valor)
