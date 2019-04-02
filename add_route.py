from pprint import pprint

import requests


def main():
    response = requests.post('http://localhost:8001/services/my-service/routes', data={
        "hosts": 'my-service.dev'
    })

    pprint(response.json())


if __name__ == '__main__':
    main()
