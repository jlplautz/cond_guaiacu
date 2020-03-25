from django.test import TestCase


# instanciar um testcase do Django na variavel _test_case
# _test_case => protegido para ninguem utilizar esta instancia
_test_case = TestCase()


# criar uma função assert_contains que vai receber o metodo assertContains
# observe que foram removidos os parenteses da função pois nao queremos pegar
# o retorno da execução da função, mas sim acessar o proprio metodo
# Desta maneira então expomos todos os metodos que forem necessario de testcase conforme
# for necessario
assert_contains = _test_case.assertContains
