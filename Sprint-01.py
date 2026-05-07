# --------- ENTRADA DE DADOS ---------

# 1.nome e tipo de usuário
def nome_e_tipo_usuario():
    nome = input("Digite seu nome: ")

    print("\n Tipos de usuários:")
    print("1 -- REGULAR")
    print("2 -- PREMIUM")
    print("3 -- CONDOMÍNIO")

    while True:
        try:
            tipo = int(input("Escolha (1, 2 ou 3): "))
            if tipo >= 1 and tipo <= 3:
                break
            else:
                print("Precisa ser números de 1 a 3 ")
        except:
            print("\nDigite apenas números!")
    return nome, tipo


# 3.carregador
def carregador_kw():
    print("\nTipos de carregador:")
    print("1 - Lento   (7.4 kW)")
    print("2 - Normal  (11 kW)")
    print("3 - Rápido  (22 kW)")

    while True:
        try:
            potencia_carregador = int(input("Escolha (1, 2 ou 3): "))
            if potencia_carregador >= 1 and potencia_carregador <= 3:
                break
            else:
                print("Precisa ser números de 1 a 3 ")
        except:
            print("\nDigite apenas números!")

    if potencia_carregador == 1:
        return 7.4
    if potencia_carregador == 2:
        return 11.0
    if potencia_carregador == 3:
        return 22.0

# 3.duração da sessão
def duracao_sessao():
    while True:
        try:
            duracao = float(input("\nDuração da sessão: "))
            if duracao > 0:
                break
            else:
                print("\nApenas números maiores que zero!")
        except:
            print("\nDigite apenas números!")


# --------- CÁLCULO E CONVERSÃO DOS DADOS ---------

# 3.1 conversão do tempo de duração da sessão
    while True:
        try:
            unidade = str(input("Unidade (h)oras ou (m)inutos: ")).lower()
            if unidade == "h" or unidade == "m":
             break
            else:
                print("Digite apenas as letra *h* ou *m* ")
        except:
         print("\nDigite somente a letra * h * para horas e a letra * m * para minutos")

    if unidade == "m":
        duracao_horas = duracao / 60
    else:
        duracao_horas = duracao
        print(f"Sua sessão te a duração de: {duracao_horas: .2f} horas")
    return duracao_horas

# 4. calcular(potencia, horas, tipo)
def calcular(potencia, duracao_horas, tipo):
    energia = potencia * duracao_horas

    if tipo == 1:
        tarifa = 1.50
    if tipo == 2:
        tarifa = 1.20
    if tipo == 3:
        tarifa = 1.35

    custo = energia * tarifa

    return energia, custo

# --------- EXIBIÇÃO DO RELATÓRIO ---------

# 5. Exibição do Relatório
def exibir_relatorio(nome, tipo, potencia, horas, energia, custo):
    print("\n═══════════════════════════════")
    print("      RELATÓRIO DA SESSÃO      ")
    print("═══════════════════════════════")
    print(f"Usuário:  {nome}")
    print(f"Tipo:     {tipo}")
    print(f"Potência: {potencia} kW")
    print(f"Duração:  {horas:.2f} horas")
    print(f"Energia:  {energia:.2f} kWh")
    print(f"Custo:    R$ {custo:.2f}")
    print("═══════════════════════════════")

# --------- CHAMANDO E CONECTANDO AS FUNÇÕES ---------

def main():
    nome, tipo = nome_e_tipo_usuario()
    potencia = carregador_kw()
    horas = duracao_sessao()

    energia, custo = calcular(potencia, horas, tipo)
    exibir_relatorio(nome, tipo, potencia, horas, energia, custo)

if __name__ == "__main__":
    main()



