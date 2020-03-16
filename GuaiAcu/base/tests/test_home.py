from django.test import Client


# Create your tests here.

def test_status_code(client: Client):
    """
    Quando accessamos nosso site fazemos uma chamada do tipo get
    logo na raiz da aplicação. Justamente a view que construimos
    Emulando um request o protocolo http vai retornar um response.
    Aqui queremos nos certificar que esta resposta retornou com sucesso
    :param client:
    :return:
    """
    resp = client.get('/')
    assert resp.status_code == 200
