from db import Base
from mixins import TimeMixin
from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship


class User(Base, TimeMixin):  # type: ignore
    __tablename__ = "users"
    __table_args__ = {"extend_existing": True}

    id = Column(Integer, primary_key=True, autoincrement=True)
    display_id = Column(String(128), unique=True)
    test_id = Column(String(128), unique=True)
    is_admin = Column(Boolean, default=False, server_default="0")
    is_deleted = Column(Boolean, default=False, server_default="0")
    backgrounds = relationship("Background", back_populates="user")
    effects = relationship("Effect", back_populates="user")
    engines = relationship("Engine", back_populates="user")
    levels = relationship("Level", back_populates="user")
    particles = relationship("Particle", back_populates="user")
    skins = relationship("Skin", back_populates="user")
    likes = relationship("Like", back_populates="user")
    favorites = relationship("Favorites", back_populates="user")