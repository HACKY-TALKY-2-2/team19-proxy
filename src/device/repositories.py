import re

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

    def get_device_by_device_token(self, device_token: str):
        raw_sql: TextClause = text("""
            SELECT id, device_token, St_AsText(position)
            FROM devices
            WHERE device_token = :device_token
            """)
        result = self.session.execute(
            raw_sql,
            {"device_token": device_token},
        ).fetchone()
        return {
            "id": result[0],
            "device_token": result[1],
            "longitude": float(re.findall(r"[-+]?\d*\.\d+|\d+", result[2])[1]),
            "latitude": float(re.findall(r"[-+]?\d*\.\d+|\d+", result[2])[0]),
        }

    def get_closest_camera_to_position(self, longitude: float, latitude: float):
        raw_sql: TextClause = text("""
            SELECT address,
                   St_AsText(position),
                   name,
                   ST_Distance_Sphere(
                       Point(:longitude, :latitude),
                       Point(ST_Y(position), ST_X(position))
                   ) AS distance
            FROM cameras
            ORDER BY distance
            LIMIT 1
            """)
        result = self.session.execute(
            raw_sql,
            {
                "longitude": longitude,
                "latitude": latitude,
            },
        ).fetchone()
        return {
            "address": result[0],
            "longitude": float(re.findall(r"[-+]?\d*\.\d+|\d+", result[1])[1]),
            "latitude": float(re.findall(r"[-+]?\d*\.\d+|\d+", result[1])[0]),
            "name": result[2],
            "distance": result[3],
        }
