def validacao(senha):
    especiais = '!@#$%^&*()-+'
    try:
        assert any(c.isdigit() for c in senha)
        assert any(c.islower() for c in senha)
        assert any(c.isupper() for c in senha)
        assert any(c in especiais for c in senha)
        assert len(senha) > 8
        assert len(senha) == len(set(senha))
        return True

    except AssertionError:
        return False
