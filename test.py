import shadowhash.__main__ as shadowhash
from pyescrypt import Yescrypt, Mode

# d=shadowhash.yescrypt_hash("apple",b"jUpCiSe2XfOy7mV1FPHrF0")
# d = Yescrypt(
#         mode=Mode.MCF,
#         n=2**12,
#         r=32,
#         p=1,
#         t=0,
#     ).digest(
#         "apple".encode(),
#         salt=b"jUpCiSe2XfOy7mV1FPHrF0"
#     ).decode()
d = shadowhash.sha512_crypt_hash("qw",b"jUpCiSe2XfOy7mV1FPHrF0")
print(d)