from app import app,db
from app.models import Book,Writer,User,ListOfBorrow

@app.shell_context_processor
def make_shell_context():
   return {
       'db':db,
       'Book':Book,
       'Writer':Writer,
       'User':User,
       'ListOfBorrow':ListOfBorrow         
   }