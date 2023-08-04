from utilid import menulst
from utilid import arquivo
from time import sleep


a = "cursoemvideo.txt"

if not arquivo.arqexiste(a):
    arquivo.criararq(a)


while True:
    r = menulst.menu(
        ["Ver pessoas cadastradas", "Cadastrar pessoas", "Sair do sistema"]
    )
    if r == 1:
        arquivo.lerarq(a)
    elif r == 2:
        menulst.cab("CADASTRAR NOVA PESSOA")
        n = str(input("Nome: "))
        i = menulst.leiaint("Idade: ")
        arquivo.cadastro(a, n, i)
    elif r == 3:
        menulst.cab("Saindo do sistema...")
        break
    else:
        print("\033[31Digite um valor valido!\033[m")
    sleep(3)
