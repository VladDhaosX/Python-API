from database import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    create_date = db.Column(db.DateTime, default=db.func.current_timestamp())

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "create_date": self.create_date,
        }

    @classmethod
    def create(cls, name):
        new_user = cls(name=name)
        db.session.add(new_user)
        db.session.commit()
        return new_user
