from __future__ import annotations

from typing import Protocol, TYPE_CHECKING, final

import aiohttp

if TYPE_CHECKING:
    pass

__all__ = (
    "IUserService",
    "UserController",
)


class IUserService(Protocol):
    def get_users(self, amount: int): ...


@final
class UserController:
    """Class work on API https://randomuser.me/."""

    user_api = "https://randomuser.me/api"

    async def get_users(self, *, amount: int) -> list[dict]:
        async with aiohttp.ClientSession() as session:
            async with session.get(
                self.user_api,
                params=[
                    ("results", amount),
                ],
            ) as response:
                response = await response.json()

        users = response.get("results")

        if users is None:
            return {}

        return users
