import base64 
print("""
instagram : kedy.coder
youtube : kedy coder
1- Encrypt
2- Decrypt
""")

kedycoder = input("1 or 2 ? -> ")
if kedycoder == "1" : 
    message = input("String => ")
    message_bytes = message.encode('ascii')
    base64_bytes = base64.b64encode(message_bytes)
    base64_message = base64_bytes.decode('ascii')
    print(f"Hash -> {base64_message}")
if kedycoder == "2" : 
    base64_string = input("Hash => ")
    base64_bytes = base64_string.encode("ascii")
    sample_string_bytes = base64.b64decode(base64_bytes)
    sample_string = sample_string_bytes.decode("ascii")
    print(f"Cracked -> : {sample_string}")
