from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker

engine = create_async_engine('sqlite+aiosqlite:///Subs.sqlite3')
async_session = async_sessionmaker(engine)

class Base(DeclarativeBase, AsyncAttrs):
    pass


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    tg_id = mapped_column(BigInteger) 

async def async_main():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

