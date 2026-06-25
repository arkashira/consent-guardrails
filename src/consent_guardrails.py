import json
from dataclasses import dataclass
from typing import List

@dataclass
class Legislation:
    name: str
    expert_input: bool
    public_consultation: bool
    data_protection: bool
    consent: bool
    review_date: str

class ConsentGuardrails:
    def __init__(self):
        self.legislations = []

    def add_legislation(self, legislation: Legislation):
        self.legislations.append(legislation)

    def get_legislations(self):
        return self.legislations

    def review_legislation(self, name: str):
        for legislation in self.legislations:
            if legislation.name == name:
                return legislation
        return None

    def update_legislation(self, name: str, review_date: str):
        for legislation in self.legislations:
            if legislation.name == name:
                legislation.review_date = review_date
                return
        raise ValueError("Legislation not found")

    def validate_legislation(self, legislation: Legislation):
        if not legislation.expert_input or not legislation.public_consultation:
            raise ValueError("Legislation must be informed by expert input and public consultation")
        if not legislation.data_protection or not legislation.consent:
            raise ValueError("Legislation must prioritize data protection and consent")
