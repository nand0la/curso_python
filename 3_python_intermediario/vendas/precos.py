import vendas.formata as frm

def almento(valor, porcetagem, formata=False):
    valor = valor + (valor * (porcetagem / 100))
    
    if formata:
        return frm.formata_real(valor)
    
    return valor
    

def reducao(valor, porcetagem):
    return valor - (valor * (porcetagem / 100))