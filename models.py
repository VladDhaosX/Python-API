from database import db

class Station(db.Model):
    __tablename__ = 'Station'

    Id = db.Column(db.Integer, primary_key=True)
    Station = db.Column(db.String)
    Name = db.Column(db.String)
    StatusId = db.Column(db.Integer)
    CreatedDate = db.Column(db.DateTime)

    def __repr__(self):
        return f'<Station {self.Id} {self.Name}>'
