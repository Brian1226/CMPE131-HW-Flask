from app import db

class User(db.Model):
   """
   Holds users' data:

   id (int) = user's unique identification
   'author' (String) = unique name that lets other users determine who sent the messages
   'message' = the text that users sent
   """

   # id (int)
   id = db.Column(db.Integer, primary_key = True)

   # author (string, unique, can't be null)
   author = db.Column(db.String, unique = True, nullable = False)

   # message (link to Messages table)
   message = db.relationship('Messages', backref = 'author', lazy = 'dynamic')

   # outputs <User: AUTHOR_GOES_HERE>
   # ex. <User : Brian>
   def __repr__(self):
       return '<User: {}>'.format(self.author)


class Messages(db.Model):
   """
   Holds data for messages:

   id (int) = the message's unique identification
   'message' (String) = the text that users sent
   'user_id' (String) = the user's unique identification
   """

   # id (int)
   id = db.Column(db.Integer, primary_key = True)

   # message (string, not unique, can't be null)
   message = db.Column(db.String, unique = False, nullable = False)

   # user_id link to id (int)
   user_id = db.Column(db.Integer, db.ForeignKey('user.id'))

   # write __repr__ that outputs
   # <Message: MESSAGE_GOES_HERE>
   # replace MESSAGE_GOES_HERE with the message
   # ex. <Message : Hello, guys!>
   def __repr__(self):
       return '<Message: {}>'.format(self.message)
