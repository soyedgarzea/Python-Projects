import hashlib
import sys
import requests


def request_api_data(query_char: str):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)

    if res.status_code != 200:
        raise RuntimeError(f'Error fetching {res.url}')

    return res

def get_leak_count(hashes: tuple[str, int], has_to_check: str) -> int: # type: ignore
    hashes = (line.split(':') for line in hashes.text.splitlines()) # type: ignore

    for h, count in hashes: # type: ignore
        if h == has_to_check: # type: ignore
            return count  # type: ignore
    return 0


def pwned_api_check(password: str):
    sha1_pass = hashlib.sha1(password.encode(('utf-8'))).hexdigest().upper()
    first5_char, tail = sha1_pass[:5], sha1_pass[5:]
    response = request_api_data((first5_char))

    return get_leak_count(response, tail) # type: ignore

def main(args: list[str]):
    for password in args:
        count = pwned_api_check(password)

        if count:
            print(f'{password} was found {count} times...')
        else:
            print(f'{password} was not found. You are good to go!')
    return 'done'

if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
