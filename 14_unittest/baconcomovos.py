
def bacon_com_ovos(n):
    assert isinstance(n, int), 'O valor tem que ser um inteiro'
    
    if n % 5 == 0 and n % 3 == 0: return 'Bacon com Ovos'
    if n % 5 == 0: return 'Bacon'
    if n % 3 == 0: return 'Ovos'

    return 'Passar fome'