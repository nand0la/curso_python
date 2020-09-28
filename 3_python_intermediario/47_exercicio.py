def saudar(msg="Olá", nome="Usuário"):
    print(f"{msg}, {nome}")


saudar(msg="Koe", nome="Fernando")


# ========================


def soma_tres_valores(x, y, z):
    print(x + y + z)


soma_tres_valores(10, 15, 20)


# ==========================


def soma_porcetagem(valor, percente):
    porcetagem = (percente / 100) * valor
    return valor + porcetagem


print(soma_porcetagem(100, 10))


# ==============================


def fizz_buzz(n):
    if n % 5 == 0 and n % 3 == 0:
        return "fizz buzz"

    elif n % 2 == 0:
        return "fizz"

    elif n % 5 == 0:
        return "buzz"

    else:
        return n


print(fizz_buzz(15))
