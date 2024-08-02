from db.uow import UnitOfWork
from services import get_simple_service


class TestCreateSimple:
    """Create simple test."""

    async def test_success(self, db_uow: UnitOfWork) -> None:
        """Success create simple test."""
        s_service = get_simple_service(db_uow)
        a = await s_service.create("test")
        async with db_uow:
            v = await db_uow.simple_table.get_one(id=a.id)
        assert v.name == a.name

        a = await s_service.create("sssss")
        async with db_uow:
            v = await db_uow.simple_table.get_one(id=a.id)
        assert v.name == a.name
