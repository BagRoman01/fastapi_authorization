import logging

from app.core.security import hash_password
from app.exceptions.auth_exceptions import (
    UserAlreadyExistsError,
    UserNotFoundError,
)
from app.models.db.user import User
from app.models.schemas.user import UserCreate
from app.utils.uow import IUnitOfWork

log = logging.getLogger(__name__)


class UsersService:
    def __init__(self, uow: IUnitOfWork):
        self.uow = uow

    async def register_user(self, user: UserCreate):
        log.info(f"Регистрация пользователя: почта: {user.email}, пароль: {user.password}")

        async with self.uow:
            log.info('Ищем пользователя в базе данных')
            existing_user = await self.uow.user_repos.find_by_email(user.email)
            if existing_user:
                log.warning('Пользователь с таким именем уже существует!')
                raise UserAlreadyExistsError(email=existing_user.email)
            hashed_pwd = await hash_password(user.password)
            user_dict = user.model_dump()
            user_dict["hashed_password"] = hashed_pwd
            del user_dict["password"]
            query_exec = await self.uow.user_repos.add_one(user_dict)
            result = User.model_validate(query_exec)
            await self.uow.commit()
            return result

    async def get_user_from_db(
            self,
            user_id: int = None,
            email: str = None
    ) -> User:
        async with self.uow:
            if user_id and email:
                raise ValueError("Both user_id and email cannot be specified simultaneously.")

            if user_id:
                user = await self.uow.user_repos.find_by_id(user_id)
            elif email:
                user = await self.uow.user_repos.find_by_email(email)

            if not user:
                raise UserNotFoundError

            user_from_db = User(id=user.id, email=user.email, hashed_password=user.hashed_password)
            return user_from_db
