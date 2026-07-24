# lib/converter.py
import math

def celsius_to_fahrenheit(c):
    return c * 9 / 5 + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5 / 9

def celsius_to_kelvin(c):
    if c < -273.15:
        raise ValueError("A temperatura não pode estar abaixo do zero absoluto.")
    return c + 273.15

def kelvin_to_celsius(k):
    if k < 0:
        raise ValueError("A temperatura não pode estar abaixo do zero absoluto.")
    return k - 273.15

def fahrenheit_to_kelvin(f):
    celsius = fahrenheit_to_celsius(f)
    kelvin = celsius_to_kelvin(celsius)
    return kelvin

def kelvin_to_fahrenheit(k):
    celsius = kelvin_to_celsius(k)
    fahrenheit = celsius_to_fahrenheit(celsius)
    return fahrenheit

# Funções de Verificação

def is_water_freezing(value: float, scale: str) -> bool:
    """
    Verifica se a temperatura corresponde ao ponto de congelamento da água.
    """
    # 1. Validação de tipo e escala
    if not isinstance(value, (int, float)):
        raise TypeError("O valor da temperatura deve ser um número.")
    
    supported_scales = {'celsius', 'fahrenheit', 'kelvin'}
    if scale.lower() not in supported_scales:
        raise ValueError(f"Escala '{scale}' desconhecida ou não suportada.")

    # 2. Conversão interna para Celsius
    celsius_value = 0
    if scale.lower() == 'celsius':
        celsius_value = value
    elif scale.lower() == 'fahrenheit':
        celsius_value = fahrenheit_to_celsius(value)
    elif scale.lower() == 'kelvin':
        celsius_value = kelvin_to_celsius(value)

    # 3. Validação de zero absoluto (seguindo o modelo)
    if celsius_value < -273.15:
        raise ValueError("A temperatura não pode estar abaixo do zero absoluto.")

    # 4. Lógica principal da função
    return math.isclose(celsius_value, 0)

def is_water_boiling(value: float, scale: str) -> bool:
    """
    Verifica se a temperatura corresponde ao ponto de ebulição da água.
    """
    # 1. Validação de tipo e escala
    if not isinstance(value, (int, float)):
        raise TypeError("O valor da temperatura deve ser um número.")
    
    supported_scales = {'celsius', 'fahrenheit', 'kelvin'}
    if scale.lower() not in supported_scales:
        raise ValueError(f"Escala '{scale}' desconhecida ou não suportada.")

    # 2. Conversão interna para Celsius
    celsius_value = 0
    if scale.lower() == 'celsius':
        celsius_value = value
    elif scale.lower() == 'fahrenheit':
        celsius_value = fahrenheit_to_celsius(value)
    elif scale.lower() == 'kelvin':
        celsius_value = kelvin_to_celsius(value)

    # 3. Validação de zero absoluto (seguindo o modelo)
    if celsius_value < -273.15:
        raise ValueError("A temperatura não pode estar abaixo do zero absoluto.")

    # 4. Lógica principal da função
    return math.isclose(celsius_value, 100)

def get_water_state(value: float, scale: str) -> str:
    """
    Retorna o estado físico da água (Sólido, Líquido ou Gasoso).
    """
    # 1. Validação de tipo e escala
    if not isinstance(value, (int, float)):
        raise TypeError("O valor da temperatura deve ser um número.")
    
    supported_scales = {'celsius', 'fahrenheit', 'kelvin'}
    if scale.lower() not in supported_scales:
        raise ValueError(f"Escala '{scale}' desconhecida ou não suportada.")

    # 2. Conversão interna para Celsius
    celsius_value = 0
    if scale.lower() == 'celsius':
        celsius_value = value
    elif scale.lower() == 'fahrenheit':
        celsius_value = fahrenheit_to_celsius(value)
    elif scale.lower() == 'kelvin':
        celsius_value = kelvin_to_celsius(value)

    # 3. Validação de zero absoluto (seguindo o modelo)
    if celsius_value < -273.15:
        raise ValueError("A temperatura não pode estar abaixo do zero absoluto.")

    # 4. Lógica principal da função
    if math.isclose(celsius_value, 0):
        return "Sólido/Líquido (ponto de congelamento)"
    if math.isclose(celsius_value, 100):
        return "Líquido/Gasoso (ponto de ebulição)"

    if celsius_value < 0:
        return "Sólido"
    if celsius_value > 100:
        return "Gasoso"
    
    return "Líquido"
