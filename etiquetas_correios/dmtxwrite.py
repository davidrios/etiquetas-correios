from base64 import b64encode
from subprocess import check_output, CalledProcessError
from uuid import uuid4


try:
    check_output('dmtxwrite --help', shell=True)
except CalledProcessError:
    raise Exception('O programa dmtxwrite (dmtx-utils) precisa estar instalado para usar este módulo.')


def renderizar_svg(dados):
    dados_codificados = dados.encode('utf8')
    id_elemento = str(uuid4())

    svg_data = check_output('dmtxwrite -fSVG -m1 -d2', shell=True, input=dados_codificados).decode('utf8')
    svg_data = svg_data.replace('dmtx_0001', id_elemento)
    svg_data = svg_data.replace('"svg2"', 'svg-' + id_elemento)
    return svg_data


def renderizar_png(dados):
    png_data = check_output('dmtxwrite -fPNG -r300 -m1 -d2', shell=True, input=dados.encode('utf8'))
    return '<img src="data:image/png;base64,{}" />'.format(b64encode(png_data).decode('ascii'))
