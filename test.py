def replacecode(content):
    content = content.replace('base64', "__import__(binascii.unhexlify(b'626173653634').decode())")
    return content
