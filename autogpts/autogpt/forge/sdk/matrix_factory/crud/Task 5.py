# Import the necessary modules
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

# Create a base class for all database models
Base = declarative_base()

# Define the User model
class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    email = Column(String)
    
    # Define a relationship with the Post model
    posts = relationship('Post', backref='author')
    
    def __repr__(self):
        return f'<User(name={self.name}, email={self.email})>'
    
# Define the Post model
class Post(Base):
    __tablename__ = 'posts'
    
    id = Column(Integer, primary_key=True)
    title = Column(String)
    content = Column(String)
    author_id = Column(Integer, ForeignKey('users.id'))
    
    def __repr__(self):
        return f'<Post(title={self.title}, content={self.content})>'