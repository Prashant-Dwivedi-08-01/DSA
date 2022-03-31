# x = 1000000009
# n = 2000000
# ans  = (( 10 % x )**n) % x
# print(x**n)
# 


from cryptography.fernet import Fernet


key = b'ib5ZXgHt8nw-coZV2JtoAsrf9i8fzJPdxzw7iktOYo8='
passw = b'gAAAAABiRAp6g3hI17Bt7b5YxT0iJsqqRvehJ2ZPOor6eUKkNwAynG2Dt2WkaKUOTjASn5_bs6TQoZ-6GoCWCpSd0-HeDSDHlg=='

fernet = Fernet(key)
decMessage = fernet.decrypt(passw).decode()
print(decMessage)