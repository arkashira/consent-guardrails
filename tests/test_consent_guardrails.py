from consent_guardrails import ConsentGuardrails, Legislation

def test_add_legislation():
    guardrails = ConsentGuardrails()
    legislation = Legislation("Test Legislation", True, True, True, True, "2022-01-01")
    guardrails.add_legislation(legislation)
    assert len(guardrails.get_legislations()) == 1

def test_get_legislations():
    guardrails = ConsentGuardrails()
    legislation1 = Legislation("Test Legislation 1", True, True, True, True, "2022-01-01")
    legislation2 = Legislation("Test Legislation 2", True, True, True, True, "2022-01-02")
    guardrails.add_legislation(legislation1)
    guardrails.add_legislation(legislation2)
    assert len(guardrails.get_legislations()) == 2

def test_review_legislation():
    guardrails = ConsentGuardrails()
    legislation = Legislation("Test Legislation", True, True, True, True, "2022-01-01")
    guardrails.add_legislation(legislation)
    reviewed_legislation = guardrails.review_legislation("Test Legislation")
    assert reviewed_legislation.name == "Test Legislation"

def test_update_legislation():
    guardrails = ConsentGuardrails()
    legislation = Legislation("Test Legislation", True, True, True, True, "2022-01-01")
    guardrails.add_legislation(legislation)
    guardrails.update_legislation("Test Legislation", "2022-01-02")
    updated_legislation = guardrails.review_legislation("Test Legislation")
    assert updated_legislation.review_date == "2022-01-02"

def test_validate_legislation():
    legislation = Legislation("Test Legislation", False, True, True, True, "2022-01-01")
    try:
        ConsentGuardrails().validate_legislation(legislation)
        assert False
    except ValueError as e:
        assert str(e) == "Legislation must be informed by expert input and public consultation"

def test_validate_legislation_data_protection():
    legislation = Legislation("Test Legislation", True, True, False, True, "2022-01-01")
    try:
        ConsentGuardrails().validate_legislation(legislation)
        assert False
    except ValueError as e:
        assert str(e) == "Legislation must prioritize data protection and consent"
