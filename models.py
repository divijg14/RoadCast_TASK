from app import db

class Employees(db.Model):
    __tablename__ = 'Employees'


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String())
    age = db.Column(db.Integer)
    role = db.Column(db.String())

    def __init__(self, name, age, role):
        self.name = name
        self.age = age
        self.role = role
    
    def serialize(self):
        return { 
            'name': self.name,
            'age': self.age,
            'role':self.role
        }

class Jobs(db.Model):
    __bind_key__ = 'mysql'
    __tablename__ = 'jobs'


    id = db.Column(db.Integer, primary_key=True)
    job_id = db.Column(db.Integer)
    role = db.Column(db.String())
    
    def __init__(self, job_id, role):
        self.job_id = job_id
        self.role = role

    def serialize(self):
        return { 
            'job_id': self.job_id,
            'role':self.role
        }