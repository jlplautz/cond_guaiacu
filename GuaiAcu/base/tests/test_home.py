import pytest
from django.urls import reverse
from GuaiAcu.django_assertions import assert_contains


@pytest.fixture
def resp(client):
    resp = client.get(reverse('home'))
    return resp


# Create your tests here.
def test_status_code(resp):
    """
    Quando accessamos nosso site fazemos uma chamada do tipo get
    logo na raiz da aplicação. Justamente a view que construimos
    Emulando um request o protocolo http vai retornar um response.
    Aqui queremos nos certificar que esta resposta retornou com sucesso
    :param client:
    :return:
    """
    assert resp.status_code == 200


def test_titulo(resp):
    """
    Vamos testar o titulo da homepage e vamos utilizar aquela função assertContains
    Esta função recebe a resposta que foi gerada atraves da  execusão do metodo da views
    e como segundo parametro ela vai se certificar se existe uma string dentro desta
    responta com um formato especifico
    :param client:
    :return:
    """
    assert_contains(resp, '<title>Condominio Guai-Açu</title>')


def test_home_link(resp):
    assert_contains(resp, f'href="{reverse("home")}">Condomínio Guai-Açu</a>')
