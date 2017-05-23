from codecs import open
from os import path

try:
    from jinja2 import Environment, PackageLoader, select_autoescape
except ImportError:
    raise Exception('Para usar a geração de HTML você deve instalar a dependência adicional [gerar-html].')

MY_DIR = path.dirname(__file__)

env = Environment(
    loader=PackageLoader('etiquetas_correios', 'templates'),
    autoescape=select_autoescape(['html', 'xml'])
)


def gerar_html(etiquetas, renderizar_data_matrix, css='pimaco6184'):
    template = env.get_template('etiquetas.html')

    with open(path.join(MY_DIR, 'templates', css + '.css'), 'r', encoding='utf8') as fp:
        codigo_css = fp.read()

    with open(path.join(MY_DIR, 'templates', 'JsBarcode.code128.min.js'), 'r', encoding='utf8') as fp:
        codigo_js = fp.read()

    return template.render(
        etiquetas=etiquetas,
        renderizar_data_matrix=renderizar_data_matrix,
        codigo_css=codigo_css,
        codigo_js=codigo_js)
