from pprint import pprint

import requests


def main():
    response = requests.post('http://localhost:8001/services/my-service/plugins', data={
        "name": "jwt"
    })

    return response


if __name__ == '__main__':
    pprint(main().json())
