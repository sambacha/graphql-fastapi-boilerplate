from typing import cast

from fastapi import Request

from backend.config import Configuration
from backend.types import AppState


async def get_config(request: Request) -> Configuration:
    state = cast(AppState, request.app.state)

    return state.config
