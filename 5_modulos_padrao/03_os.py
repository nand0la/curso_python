import os

path = "/home/fernando/Downloads/tbbt12"
find_term = "24"

for raiz, diretorios, arquivos in os.walk(path):
    print(raiz)

    for arquivo in arquivos:

        if find_term in arquivo:
            caminho_completo = os.path.join(path, arquivo)
            nome_arquivo, ext_arquivo = os.path.splitext(arquivo)
            tamanho_arquivo = os.path.getsize(caminho_completo)

            print(f"encontramos o arquivo: {arquivo}")
            print(f"caminho: {caminho_completo}")
            print(f"nome: {nome_arquivo}")
            print(f"extenção: {ext_arquivo}")
            print(f"tamanho: {tamanho_arquivo}")
            print()
