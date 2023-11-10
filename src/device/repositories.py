from sqlalchemy import TextClause, text
from sqlalchemy.orm import Session


class DeviceSQLRepository:
    def __init__(self, session: Session):
        self.session = session

    def create_device(self, device_token: str):
        raw_sql: TextClause = text("""
            INSERT INTO devices (device_token)
            VALUES (:device_token)
            """)
        self.session.execute(raw_sql, {"device_token": device_token})
