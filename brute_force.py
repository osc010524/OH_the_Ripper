import itertools
from tqdm import tqdm
import shadowhash.__main__ as shadowhash

special_char = ['~', '!', '@', '#', '$', '%', '^', '&', '*', '_', '-', '+', '=', '`', '|', '\\', '(', ')', '{', '}',
                '[', ']', ':', ';', '"', "'", '<', '>', ',', '.', '?', '/']
upper_char = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
              'V', 'W', 'X', 'Y', 'Z']
lower_char = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
              'v', 'w', 'x', 'y', 'z']
number = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']


def brute_force(min_length: int = 1, max_length: int = 16, required_chars: str = "",cyphertext:str="",crypto_type:int=0,crypto_salt:str=""):
    """
    Brute force attack to crack the password
    :param min_length: password minimum length
    :param max_length: password maximum length
    :param required_chars: password required characters
    :param cyphertext: cyphertext
    :param crypto_type: crypto type
    :param crypto_salt: salt
    :return: password
    """
    table = make_table(required_chars)
    crypto_func = select_crypto_type(crypto_type)

    # yescrypt_hash의 경우에는 소금이 바이트열이어야 하므로 인코딩
    if crypto_type == "y":
        crypto_salt = crypto_salt.encode()

    # 가능한 모든 길이의 비밀번호에 대해 브루트 포스 공격 시도
    for length in range(min_length, max_length + 1):
        pbar = tqdm(list(itertools.product(table, repeat=length)),desc=f"Lenght: {length}")
        for attempt in pbar:
            password = ''.join(attempt)
            password_h = crypto_func(password, crypto_salt)
            if check_password(password_h,cyphertext):
                # print(f"Found password: {password}")
                return password
    return "Not Found"

def make_table(required_chars: str = ""):
    """
    Select the character set based on the required_chars
    :param required_chars:
    s = special characters
    u = upper case characters
    l = lower case characters
    n = numbers
    :return: [list] character set
    """
    table = []
    if "s" in required_chars:
        table += special_char
    if "u" in required_chars:
        table += upper_char
    if "l" in required_chars:
        table += lower_char
    if "n" in required_chars:
        table += number
    return table

def select_crypto_type(crypto_type):
    """
    Select the crypto function based on the crypto type
    :param crypto_type:
    1 : md5crypt_hash
    2 : bcrypt_hash : blowfish
    5 : sha256_crypt_hash
    6 : sha512_crypt_hash
    y : yescrypt_hash
    :return: function
    """
    if crypto_type == "1":
        return shadowhash.md5crypt_hash
    elif crypto_type == "2":
        return shadowhash.bcrypt_hash
    elif crypto_type == "5":
        return shadowhash.sha256_crypt_hash
    elif crypto_type == "6":
        return shadowhash.sha512_crypt_hash
    elif crypto_type == "y":
        return shadowhash.yescrypt_hash

def check_password(password:str,cyphertext:str):
    """
    Check if the password is correct
    :param password:
    :param cyphertext:
    :return: [bool] True if the password is correct
    """
    if password == cyphertext:
        return True
    else:
        return False
