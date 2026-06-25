import json
from dataclasses import dataclass
from datetime import datetime
from typing import List

@dataclass
class ConsentToken:
    token: str
    timestamp: datetime

class ConsentGuardrails:
    def __init__(self):
        self.consent_history = []

    def add_consent_token(self, token: str):
        self.consent_history.append(ConsentToken(token, datetime.now()))

    def get_consent_history(self) -> List[ConsentToken]:
        return self.consent_history

    def download_consent_history(self) -> str:
        history = [{"token": token.token, "timestamp": token.timestamp.isoformat()} for token in self.consent_history]
        return json.dumps(history, indent=4)

    def authenticate(self, user_id: str, password: str) -> bool:
        # Simple authentication for demonstration purposes
        return user_id == "user" and password == "password"
