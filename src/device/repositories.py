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
        self.session.execute(
            raw_sql,
            {"device_token": device_token},
        )

    def update_device_position(
        self, device_token: str, longitude: float, latitude: float
    ):
        raw_sql: TextClause = text("""
            UPDATE devices
            SET position = ST_GeomFromText('POINT(:latitude :longitude)'),
                updated_at = NOW()
            WHERE device_token = :device_token
            """)
        self.session.execute(
            raw_sql,
            {
                "device_token": device_token,
                "longitude": longitude,
                "latitude": latitude,
            },
        )
