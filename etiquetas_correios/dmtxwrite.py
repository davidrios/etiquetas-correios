from subprocess import check_output
from uuid import uuid4


def renderizar_svg(dados):
    dados_codificados = dados.encode('utf8')
    id_elemento = str(uuid4())

    svg_data = check_output('dmtxwrite -fSVG -m1 -d2', shell=True, input=dados_codificados).decode('utf8')
    svg_data = svg_data.replace('dmtx_0001', id_elemento)
    svg_data = svg_data.replace('"svg2"', 'svg-' + id_elemento)
    return svg_data
