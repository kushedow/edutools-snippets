# simple flask app

from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def sample():
    result = []
    return dumps(result), 200


if __name__ == '__main__':
    app.run()


# check

from task import app

class TestCase(TestCase):
    def test_sort(self):
        with app.test_client() as client:

            #  проверка статуса

            resp = client.get('/sort/')
            self.assertNotEqual(404, resp.status_code, msg='Представление должно работать по урлу /sort/')

            # ожидание и реальность

            path = '/'
            expected = '...'
            resp = client.get(path)
            self.assertEqual(expected, resp.get_data(True),
                             msg=f'Неверный ответ пи запросе к {path} должно быть {expected}')
