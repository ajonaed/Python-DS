from caesarCiphar import CaesarCipher
def main():
    machine = CaesarCipher(5)
    msg = 'Abdullah Jonaed'
    secret = machine.encrypt(msg.upper())
    print(secret)
    notSecret = machine.decrypt(secret)
    print(notSecret)


if __name__ == '__main__':
    main()