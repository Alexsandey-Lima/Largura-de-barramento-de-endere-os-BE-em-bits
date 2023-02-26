def valor_em_potecia2(qtd_barramento):
    numero=qtd_barramento
    qtd_exponecial=[]
    while numero > 1 and numero%2==0:
        resto = numero % 2
        if resto == 0:
            qtd_exponecial.append(numero)
            numero=numero/2

    #print(f"""Valor de potência = {qtd_exponecial[-1]}^{len(qtd_exponecial)}""")
    return len(qtd_exponecial)
def analisando_prefixo(prefixo):
    if prefixo == 'K':
        valor_do_prefixo=1024
    if prefixo == 'M':
        valor_do_prefixo=1048576
    if prefixo == 'G':
        valor_do_prefixo =1073741824
    if prefixo == 'T':
        valor_do_prefixo =1099511627776
    return valor_em_potecia2(valor_do_prefixo)

run=True
while run == True:
    try:
        print("""K = quilo M = MEGA G = giga T = tera""")
        prefixo = input("Qual o prefixo?\n")
        valor_unitario = int(input("Qual o valor unitario?\n"))

        potencia_prefixo = analisando_prefixo(prefixo.upper())
        potencia_valor_unitario = valor_em_potecia2(valor_unitario)
        resultado=potencia_prefixo+potencia_valor_unitario
    except:
        print("valor errado tente novamente")
        continue

    print(f"Valor unitário da potencia = {potencia_valor_unitario}\n Valor da potência do prefixo {potencia_prefixo}\n resultado= {resultado} bits")
    print("====================================================================")
