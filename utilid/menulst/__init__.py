def leiaint(msg):
    while True:
        try:
            v = int(input(msg))
        except (ValueError, TypeError):
            print("\033[31mERRO, digite um valor numerico Inteiro!\033[m")
            continue
        except KeyboardInterrupt:
            print(
                "\033[34mo usuario decidiu sair antes do fim do programa terminar\033[m"
            )
            return 0
        else:
            return v


def l(t=42):
    return "-" * t


def cab(txt):
    print(l())
    print(txt.center(42))
    print(l())


def menu(lista):
    cab("\033[35mMENU PRINCIPAL\033[m")
    c = 1
    for item in lista:
        print(f"\033[33m{c} -\033[m \033[32m{item}\033[m")
        c += 1
    print(l())

    o = leiaint("\033[36mSua opçao:\033[m ")
    return o
