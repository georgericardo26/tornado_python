from sqlalchemy import Column, BigInteger, String, DateTime, Boolean
from setup.core.settings import db_settings

db = db_settings()


class Profile(db.Model):
    id = Column(BigInteger, primary_key=True, autoincrement=True)
    username = Column(String(255), unique=True, nullable=False)
    first_name = Column(String(255), nullable=True)
    last_name = Column(String(255), nullable=True)
    created_at = Column(DateTime())

    def __str__(self):
        return self.username
    
    def fullname(self):
        return self.first_name + self.last_name
 
    
class Task(db.Model):
    id = Column(BigInteger, primary_key=True)
    name = Column(String(255), unique=True, nullable=False)
    note = Column(String(255), nullable=True)
    due_date = Column(DateTime())
    completed = Column(Boolean(), default=False)
    profile = Column(Profile())
