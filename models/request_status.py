from database import db


class request_status(db.Model):
    __tablename__ = "request_status"
    id = db.Column(db.Integer, primary_key=True)
    status_key = db.Column(db.String)
    name = db.Column(db.String)

    def to_dict(self):
        return {
            "id": self.id,
            "status_key": self.status_key,
            "name": self.name,
        }

    @classmethod
    def create(cls, status_key, name):
        new_status = cls(status_key=status_key, name=name)
        db.session.add(new_status)
        db.session.commit()
        return new_status
