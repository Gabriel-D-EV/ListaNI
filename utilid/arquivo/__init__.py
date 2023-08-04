from utilid import menulst


def arqexiste(nome):
    try:
        a = open(nome, "rt")
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criararq(nome):
    try:
        a = open(nome, "wt+")
        a.close()
    except:
        print("Houve um erro ao criar o Arquivo!!")
    else:
        print("Arquivo criado com sucesso!!")


def lerarq(nome):
    try:
        a = open(nome, "rt")
    except:
        print("Houve um erro ao ler o arquivo!")
    else:
        menulst.cab("PESSOAS CADASTRADAS")
        for l in a:
            dado = l.split(";")
            if (
                len(dado) >= 2
            ):  # Verifique se a lista possui pelo menos 2 elementos antes de acessá-los
                dado[1] = dado[1].replace("\n", "")
                print(f"{dado[0]:<30}{dado[1]:>5} anos")
            else:
                print("Dados inválidos no arquivo:", l.strip())
    finally:
        a.close()


def cadastro(arq, n="desconhecido", i=0):
    try:
        a = open(arq, "at")
    except:
        print("Houve um erro ao abrir o arquivo!")
    else:
        try:
            a.write(f"{n};{i}\n")
        except:
            print("Houve um erro ao escrever!!")
        else:
            print(f"novo registro de {n} registrado!")
            a.close()
