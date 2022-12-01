import heapq
import asyncio

from aoc22.utils import get_base, read_file


async def calculate(k: int):
    running_sum = 0
    min_heap = []
    async for item in read_file(f"{get_base(__file__)}/input.txt"):
        if item == "\n":
            heapq.heappush(min_heap, running_sum)
            running_sum = 0
        else:
            running_sum += int(item)
    return sum(heapq.nlargest(k, min_heap))


async def main(k: int):
    print(f"Sum of top {k}:")
    print(await calculate(k))
    print("Done!")


if __name__ == "__main__":
    asyncio.run(main(3))
