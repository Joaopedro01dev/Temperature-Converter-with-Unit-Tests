import pytest
from main import main

def test_main_option_1_celsius_to_fahrenheit(monkeypatch, capsys):
    user_inputs = iter(["1", "100", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    main()

    captured = capsys.readouterr()
    assert "-> 100.0°C equivale a 212.00°F" in captured.out
    assert "Obrigado por usar o conversor. Até logo!" in captured.out

def test_main_option_2_fahrenheit_to_celsius(monkeypatch, capsys):
    user_inputs = iter(["2", "212", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    main()

    captured = capsys.readouterr()
    assert "-> 212.0°F equivale a 100.00°C" in captured.out
    assert "Obrigado por usar o conversor. Até logo!" in captured.out

def test_main_option_3_water_state(monkeypatch, capsys):
    user_inputs = iter(["3", "0", "c", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    main()

    captured = capsys.readouterr()
    assert "-> A 0.0°C, o estado da água é: Sólido/Líquido (ponto de congelamento)" in captured.out
    assert "Obrigado por usar o conversor. Até logo!" in captured.out

def test_main_option_4_exit(monkeypatch, capsys):
    user_inputs = iter(["4"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    main()

    captured = capsys.readouterr()
    assert "Obrigado por usar o conversor. Até logo!" in captured.out

def test_main_invalid_menu_option(monkeypatch, capsys):
    user_inputs = iter(["9", "4"])
    monkeypatch.setattr("builtins.input", lambda _: next(user_inputs))

    main()

    captured = capsys.readouterr()
    assert "Opção inválida, por favor tente novamente." in captured.out