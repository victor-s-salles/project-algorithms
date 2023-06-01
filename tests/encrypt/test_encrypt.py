from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("Victor", "C")
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(12, 5)

    assert encrypt_message("victor", 3) == "civ_rot"
    assert encrypt_message("victor", 2) == "rotc_iv"
    assert encrypt_message("victor", 6) == "rotciv"
