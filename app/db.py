import uuid
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTableUUID, SQLAlchemyUserDatabase
from sqlalchemy import String, Column, DateTime, ForeignKey, Text
from sqlalchemy.orm import DeclarativeBase, relationship
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine, async_session, async_sessionmaker
from config import settings
from fastapi_users_db_sqlalchemy.generics import GUID
from datetime import datetime
#database连接串
DATABASE_URL = settings.DATABASE_URL
#创建数据库异步引擎
engine = create_async_engine(DATABASE_URL)
#创建数据库异步会话
async_session_maker = async_sessionmaker(engine, expire_on_commit=False)

class Base(DeclarativeBase):
    pass

class User(Base, SQLAlchemyBaseUserTableUUID):
    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = "post"

    id = Column(GUID, primary_key=True, default=uuid.uuid4)
    user_id = Column(GUID, ForeignKey("user.id"), nullable=False)
    caption = Column(Text)
    url = Column(String(255), nullable=False)
    file_type = Column(String(255), nullable=False)
    file_name = Column(String(255), nullable=False)
    created_at = Column(DateTime, default=datetime.now)
    user = relationship("User", back_populates="posts")

async def create_db_and_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with async_session_maker() as session:
        yield session

async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, User)