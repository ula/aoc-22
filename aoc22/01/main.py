import heapq

from aoc22.utils import read_file


async def main(k: int, f: str):
    running_sum = 0
    min_heap = []
    async for item in read_file(f):
        if item == "\n":
            heapq.heappush(min_heap, running_sum)
            running_sum = 0
        else:
            running_sum += int(item)
    return sum(heapq.nlargest(int(k), min_heap))
