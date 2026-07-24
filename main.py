# main.py

# Importamos apenas as funções que a aplicação irá usar
from lib.converter import (
    celsius_to_fahrenheit,
    fahrenheit_to_celsius,
    get_water_state
)

def handle_c_to_f():
    """Lida com a lógica de conversão de Celsius para Fahrenheit."""
    try:
        temp_c = float(input("Digite a temperatura em Celsius: "))
        temp_f = celsius_to_fahrenheit(temp_c)
        print(f"-> {temp_c}°C equivale a {temp_f:.2f}°F\n")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido.\n")

def handle_f_to_c():
    """Lida com a lógica de conversão de Fahrenheit para Celsius."""
    try:
        temp_f = float(input("Digite a temperatura em Fahrenheit: "))
        temp_c = fahrenheit_to_celsius(temp_f)
        print(f"-> {temp_f}°F equivale a {temp_c:.2f}°C\n")
    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido.\n")

def handle_water_state_check():
    """Lida com a lógica de verificação do estado da água."""
    try:
        temp = float(input("Digite a temperatura para verificar o estado da água: "))
        scale = input("Qual a escala? (C para Celsius, F para Fahrenheit): ").lower()

        if scale == 'c':
            state = get_water_state(temp, 'celsius')
            print(f"-> A {temp}°C, o estado da água é: {state}\n")
        elif scale == 'f':
            state = get_water_state(temp, 'fahrenheit')
            print(f"-> A {temp}°F, o estado da água é: {state}\n")
        else:
            print("Erro: Escala inválida. Use 'C' ou 'F'.\n")

    except ValueError:
        print("Erro: Por favor, insira um valor numérico válido para a temperatura.\n")


def main():
    """Função principal que executa o menu da aplicação."""
    while True:
        print("--- Conversor de Temperatura Interativo ---")
        print("1. Converter de Celsius para Fahrenheit")
        print("2. Converter de Fahrenheit para Celsius")
        print("3. Verificar estado da água")
        print("4. Sair")

        choice = input("Escolha uma opção: ")

        if choice == '1':
            handle_c_to_f()
        elif choice == '2':
            handle_f_to_c()
        elif choice == '3':
            handle_water_state_check()
        elif choice == '4':
            print("Obrigado por usar o conversor. Até logo!")
            break
        else:
            print("Opção inválida, por favor tente novamente.\n")

if __name__ == "__main__":
    main()
