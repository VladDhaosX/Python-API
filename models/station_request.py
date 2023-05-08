from database import db


class station_request(db.Model):
    __tablename__ = "station_request"
    id = db.Column(db.Integer, primary_key=True)
    request_status_id = db.Column(db.Integer, db.ForeignKey("request_status.id"))
    station_id = db.Column(db.Integer, db.ForeignKey("station.id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
    create_date = db.Column(db.DateTime, default=db.func.current_timestamp())
    attention_date = db.Column(db.DateTime)
    end_attention_date = db.Column(db.DateTime)

    request_status = db.relationship("request_status", backref="station_requests")
    station = db.relationship("station", backref="station_requests")
    user = db.relationship("User", backref="station_requests")

    def to_dict(self):
        return {
            "id": self.id,
            "request_status_id": self.request_status_id,
            "station_id": self.station_id,
            "user_id": self.user_id,
            "create_date": self.create_date,
            "attention_date": self.attention_date,
            "end_attention_date": self.end_attention_date,
        }

    @classmethod
    def create(
        cls, request_status_id, station_id, user_id, attention_date=None, end_attention_date=None
    ):
        new_request = cls(
            request_status_id=request_status_id,
            station_id=station_id,
            user_id=user_id,
            attention_date=attention_date,
            end_attention_date=end_attention_date,
        )
        db.session.add(new_request)
        db.session.commit()
        return new_request
