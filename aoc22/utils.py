import os
import aiofiles
from typing import Iterator


def get_base(f) -> str:
    return os.path.dirname(os.path.realpath(f))


async def read_file(file: str) -> Iterator:
    async with aiofiles.open(file) as f:
        async for line in f:
            yield line
