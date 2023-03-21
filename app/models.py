from app import db
from datetime import datetime

class Book(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   title = db.Column(db.String(50),index=True,unique=True, nullable=False)   
   release_date = db.Column(db.Text,index=True)
    
   
   writer = db.relationship("Writer", backref="writer", lazy="dynamic")
   

   def __str__(self):
       return f"<Books {self.title}>"


class Writer(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   name = db.Column(db.String(50),index=True, nullable=False)
   lastname = db.Column(db.String(50),index=True,nullable=False) 
   book_id = db.Column(db.Integer, db.ForeignKey(Book.id)) 
   
   
   def __str__(self):
       return f"<Writer {self.name} {self.lastname}>"


class User(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   username = db.Column(db.String(100), index=True, unique=True)
   email = db.Column(db.String(200), index=True, unique=True)
   password_hash = db.Column(db.String(128))
   

   def __str__(self):
       return f"<User {self.username}>"
    

class ListOfBorrow(db.Model):
   id = db.Column(db.Integer, primary_key=True)
   book_id = db.Column(db.Integer, db.ForeignKey(Book.id))
   user_id = db.Column(db.Integer, db.ForeignKey(User.id))
   borrowDate = db.Column(db.DateTime, index=True, default=datetime.utcnow)

   def __str__(self):
       return f"< {self.book_id} {self.user_id}, {self.borrowDate}>"