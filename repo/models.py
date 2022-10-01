from datetime import datetime
from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref

from src.connect import Base, engine


class Contact(Base):
    __tablename__ = "contacts"
    id = Column(Integer, primary_key=True)
    name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now())


class Phone(Base):
    __tablename__ = 'phones'
    id = Column(Integer, primary_key=True)
    phone_number = Column(String(20), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.now())
    contact_id = Column(Integer, ForeignKey('contacts.id', ondelete="CASCADE"))
    contact = relationship(Contact, backref=backref("phones", cascade="all,delete"))


class Email(Base):
    __tablename__ = 'emails'
    id = Column(Integer, primary_key=True)
    email = Column(String(250), nullable=False, unique=True)
    created = Column(DateTime, default=datetime.now())
    contact_id = Column(Integer, ForeignKey('contacts.id', ondelete="CASCADE"))
    contact = relationship(Contact, backref=backref("emails", cascade="all,delete"))


if __name__ == '__main__':
    Base.metadata.create_all(engine)
