import pytest
import json
from consent_guardrails import ConsentGuardrails, ConsentToken

@pytest.fixture
def consent_guardrails():
    return ConsentGuardrails()

def test_add_consent_token(consent_guardrails):
    token = "example_token"
    consent_guardrails.add_consent_token(token)
    assert len(consent_guardrails.get_consent_history()) == 1
    assert consent_guardrails.get_consent_history()[0].token == token

def test_get_consent_history(consent_guardrails):
    token1 = "example_token1"
    token2 = "example_token2"
    consent_guardrails.add_consent_token(token1)
    consent_guardrails.add_consent_token(token2)
    history = consent_guardrails.get_consent_history()
    assert len(history) == 2
    assert history[0].token == token1
    assert history[1].token == token2

def test_download_consent_history(consent_guardrails):
    token = "example_token"
    consent_guardrails.add_consent_token(token)
    history = consent_guardrails.download_consent_history()
    assert json.loads(history)[0]["token"] == token

def test_authenticate(consent_guardrails):
    assert consent_guardrails.authenticate("user", "password")
    assert not consent_guardrails.authenticate("wrong_user", "password")
    assert not consent_guardrails.authenticate("user", "wrong_password")

def test_authenticate_empty_history(consent_guardrails):
    assert consent_guardrails.authenticate("user", "password")
    assert consent_guardrails.get_consent_history() == []
