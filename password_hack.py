import requests
import hashlib
import sys


# Check if your password has been hacked before.
def request_api_data(query_char):
    url = "https://api.pwnedpasswords.com/range/" + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f"Error fetching: {res.status_code}")
    return res


def get_password_leaks_count(response, hash_to_check):
    hashes = (line.split(":") for line in response.text.splitlines())
    for key, count in hashes:
        # print(key, value)
        if key.endswith(hash_to_check):
            return count

    return 0


def pwned_api_check(password):
    hash_password = hashlib.sha1(password.encode("utf-8")).hexdigest().upper()
    first5_char, tail = hash_password[:5], hash_password[5:]
    response = request_api_data(first5_char)
    print(first5_char, tail)

    return get_password_leaks_count(response, tail)


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count:
            print(f"{password} was found {count} times... you should probaly change your password")
        else:
            print(f"{password} was NOT found. carry  on!")
    return "Done!"


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

