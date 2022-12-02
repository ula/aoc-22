import os
import aiofiles
from typing import Generator


def get_base() -> str:
    return os.path.dirname(os.path.realpath(__file__))


async def read_file(file: str) -> Generator[int, None, None]:
    async with aiofiles.open(file) as f:
        async for line in f:
            yield line
