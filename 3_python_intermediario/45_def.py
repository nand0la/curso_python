def foo():
    print("Hello World")


foo()


def foo2(parameter):
    print(parameter)


foo2("Ola mundo")
foo2("Que legal")


def valore_default(msg="Ola", nome="usuario"):
    print(msg, nome)


valore_default("hello", "Fernando")
valore_default(nome="Andre", msg="Bem vindo")
