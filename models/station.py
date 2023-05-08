from database import db


class station(db.Model):
    __tablename__ = "station"
    id = db.Column(db.Integer, primary_key=True)
    station = db.Column(db.String)
    name = db.Column(db.String)
    status_id = db.Column(db.Integer)
    create_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "station": self.station,
            "name": self.name,
            "status_id": self.status_id,
            "create_date": self.create_date,
        }

    @classmethod
    def create(cls, station, name, status_id):
        new_station = cls(station=station, name=name, status_id=status_id)
        db.session.add(new_station)
        db.session.commit()
        return new_station
