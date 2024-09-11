# Função para inverter a string
def inverter_string(s):
    # Inicializar uma nova string vazia
    string_invertida = ""
    # Iterar sobre a string original de trás para frente
    for i in range(len(s) - 1, -1, -1):
        string_invertida += s[i]
    return string_invertida

# Exemplo de uso
# entrada = input("Digite a string para inverter: " )  # Recebe a entrada do usuário
string_exemplo = "A minha grama é mais verde que a grama do vizinho"
resultado = inverter_string(string_exemplo)  # Inverte a string
print("String invertida:", resultado)  # Exibe o resultado
