import pytest
from lib.converter import (celsius_to_fahrenheit, celsius_to_kelvin, fahrenheit_to_celsius, fahrenheit_to_kelvin, kelvin_to_celsius, kelvin_to_fahrenheit, is_water_freezing, is_water_boiling, get_water_state)


# CELSIUS (POSITIVE AND NEGATIVE TEMPERATURES)
def test_celsius_to_fahrenheit_conversion_with_positive_temperature():
    assert celsius_to_fahrenheit(100) == 212

def test_celsius_to_fahrenheit_conversion_with_negative_temperature():
    assert celsius_to_fahrenheit(-40) == -40

def test_celsius_to_kelvin_conversion_with_positive_temperature():
    assert celsius_to_kelvin(100) == pytest.approx(373.15)

def test_celsius_to_kelvin_conversion_with_negative_temperature():
    assert celsius_to_kelvin(-40) == pytest.approx(233.15)

def test_celsius_to_kelvin_conversion_with_temperture_below_absolute_zero():
   with pytest.raises(ValueError, match="A temperatura não pode estar abaixo do zero absoluto."):
       celsius_to_kelvin(-300)


# FAHRENHEIT (POSITIVE AND NEGATIVE TEMPERATURES)
def test_fahrenheit_to_celsius_conversion_with_positive_temperature():
    assert fahrenheit_to_celsius(212) == 100

def test_fahrenheit_to_celsius_conversion_with_negative_temperature():
    assert fahrenheit_to_celsius(-40) == -40

def test_fahrenheit_to_kelvin_conversion_with_positive_temperature():
    assert fahrenheit_to_kelvin(212) == pytest.approx(373.15)

def test_fahrenheit_to_kelvin_conversion_with_negative_temperature():
    assert fahrenheit_to_kelvin(-40) == pytest.approx(233.15)


# KELVIN (POSITIVE AND NEGATIVE TEMPERATURES)
def test_kelvin_to_celsius_conversion_with_positive_temperature():
    assert kelvin_to_celsius(373.15) == pytest.approx(100.0)

def test_kelvin_to_celsius_conversion_with_negative_temperature():
    with pytest.raises(ValueError, match="A temperatura não pode estar abaixo do zero absoluto."):
        kelvin_to_celsius(-10)

def test_kelvin_to_fahrenheit_conversion_with_positive_temperature():
    assert kelvin_to_fahrenheit(373.15) == pytest.approx(212.0)

def test_kelvin_to_fahrenheit_conversion_with_negative_temperature():
    with pytest.raises(ValueError, match="A temperatura não pode estar abaixo do zero absoluto."):
        kelvin_to_fahrenheit(-10)


# TESTS FOR THE KELVIN SCALE
def test_conversion_of_absolute_zero_from_kelvin_to_celsius():
    assert kelvin_to_celsius(0) == pytest.approx(-273.15)

def test_conversion_of_absolute_zero_from_kelvin_to_fahrenheit():
    assert kelvin_to_fahrenheit(0) == pytest.approx(-459.67)


# FREEZING POINT OF WATER ON ALL SCALES
def test_is_water_freezing_with_celsius_freezing_point():
    assert is_water_freezing(0, "celsius") is True

def test_is_water_freezing_with_fahrenheit_freezing_point():
    assert is_water_freezing(32, "fahrenheit") is True

def test_is_water_freezing_with_kelvin_freezing_point():
    assert is_water_freezing(273.15, "kelvin") is True

def test_is_water_freezing_with_uppercase_scale_name():
    assert is_water_freezing(0, "CELSIUS") is True

def test_is_water_freezing_with_celsius_not_freezing():
    assert is_water_freezing(100, "celsius") is False

def test_is_water_freezing_with_fahrenheit_not_freezing():
    assert is_water_freezing(212, "fahrenheit") is False

def test_is_water_freezing_with_kelvin_not_freezing():
    assert is_water_freezing(373.15, "kelvin") is False

def test_is_water_freezing_with_invalid_value_type():
    with pytest.raises(TypeError, match="O valor da temperatura deve ser um número."):
        is_water_freezing("0", "celsius")

def test_is_water_freezing_with_unsupported_scale():
    with pytest.raises(ValueError, match="Escala 'bah' desconhecida ou não suportada."):
        is_water_freezing(0, "bah")

def test_is_water_freezing_below_absolute_zero():
    with pytest.raises(ValueError, match="A temperatura não pode estar abaixo do zero absoluto."):
        is_water_freezing(-300, "celsius")


# BOILING POINT OF WATER ON ALL SCALES
def test_is_water_boiling_with_celsius_boiling_point():
    assert is_water_boiling(100, "celsius") is True

def test_is_water_boiling_with_fahrenheit_boiling_point():
    assert is_water_boiling(212, "fahrenheit") is True

def test_is_water_boiling_with_kelvin_boiling_point():
    assert is_water_boiling(373.15, "kelvin") is True

def test_is_water_boiling_with_uppercase_scale_name():
    assert is_water_boiling(100, "CELSIUS") is True

def test_is_water_boiling_with_celsius_not_boiling():
    assert is_water_boiling(0, "celsius") is False

def test_is_water_boiling_with_fahrenheit_not_boiling():
    assert is_water_boiling(32, "fahrenheit") is False

def test_is_water_boiling_with_kelvin_not_boiling():
    assert is_water_boiling(273.15, "kelvin") is False

def test_is_water_boiling_with_invalid_value_type():
    with pytest.raises(TypeError, match="O valor da temperatura deve ser um número."):
        is_water_boiling("100", "celsius")

def test_is_water_boiling_with_unsupported_scale():
    with pytest.raises(ValueError, match="Escala 'bah' desconhecida ou não suportada."):
        is_water_boiling(100, "bah")

def test_is_water_boiling_below_absolute_zero():
    with pytest.raises(ValueError, match="A temperatura não pode estar abaixo do zero absoluto."):
        is_water_boiling(-300, "celsius")


# GET WATER STATE
@pytest.mark.parametrize("valor, escala, estado_esperado", [
    (-10, "celsius", "Sólido"),
    (20, "fahrenheit", "Sólido"), 
    (200, "kelvin", "Sólido"),

    (0, "celsius", "Sólido/Líquido (ponto de congelamento)"),
    (32, "fahrenheit", "Sólido/Líquido (ponto de congelamento)"),
    (273.15, "kelvin", "Sólido/Líquido (ponto de congelamento)"),

    (25, "celsius", "Líquido"),
    (77, "fahrenheit", "Líquido"),
    (298.15, "kelvin", "Líquido"),

    (100, "celsius", "Líquido/Gasoso (ponto de ebulição)"),
    (212, "fahrenheit", "Líquido/Gasoso (ponto de ebulição)"),
    (373.15, "kelvin", "Líquido/Gasoso (ponto de ebulição)"),

    (150, "celsius", "Gasoso"),
    (300, "fahrenheit", "Gasoso"),
    (400, "kelvin", "Gasoso"),
])
def test_get_water_state_valid_temperatures(valor, escala, estado_esperado):
    assert get_water_state(valor, escala) == estado_esperado

def test_get_water_state_with_invalid_value_type():
    with pytest.raises(TypeError, match="O valor da temperatura deve ser um número."):
        get_water_state("25", "celsius")

def test_get_water_state_with_unsupported_scale():
    with pytest.raises(ValueError, match="Escala 'bah' desconhecida ou não suportada."):
        get_water_state(25, "bah")

def test_get_water_state_below_absolute_zero():
    with pytest.raises(ValueError, match="A temperatura não pode estar abaixo do zero absoluto."):
        get_water_state(-300, "celsius")

# FREEZING POINT DIRECT CONVERSIONS
def test_celsius_freezing_point_conversions():
    assert celsius_to_fahrenheit(0) == 32
    assert celsius_to_kelvin(0) == pytest.approx(273.15)

def test_fahrenheit_freezing_point_conversions():
    assert fahrenheit_to_celsius(32) == 0
    assert fahrenheit_to_kelvin(32) == pytest.approx(273.15)

def test_kelvin_freezing_point_conversions():
    assert kelvin_to_celsius(273.15) == pytest.approx(0.0)
    assert kelvin_to_fahrenheit(273.15) == pytest.approx(32.0)