import os
from bs4 import BeautifulSoup


def get_soup():
    html_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'index.html')
    with open(html_path, 'r', encoding='utf-8') as f:
        content = f.read()
    return BeautifulSoup(content, 'html.parser')


def test_title():
    soup = get_soup()
    assert soup.title.string == 'InvaderGame'


def test_canvas_exists():
    soup = get_soup()
    canvas = soup.find('canvas', id='gameCanvas')
    assert canvas is not None
    assert canvas.get('width') == '600'
    assert canvas.get('height') == '400'


def test_script_tag_present():
    soup = get_soup()
    scripts = soup.find_all('script')
    assert len(scripts) > 0
