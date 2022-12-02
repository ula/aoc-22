from aoc22.utils import read_file

SCORES = {"A": 0, "B": 1, "C": 2}  # rock,  # paper  # scissor
WIN = 6
DRAW = 3
LOOSE = 0


async def play(p1: int, p2: int) -> int:
    if (p1 + 1) % 3 == p2:  # win
        return WIN
    elif p1 == p2:  # draw
        return DRAW
    else:
        return LOOSE


async def winning_play(p: str) -> str:
    for k, v in SCORES.items():
        if p != k and await play(SCORES[p], v) == WIN:
            return k


async def loosing_play(p: str) -> str:
    for k, v in SCORES.items():
        if p != k and await play(SCORES[p], v) == LOOSE:
            return k


async def part1(f: str):
    mapping = {"X": "A", "Y": "B", "Z": "C"}
    total_score = 0
    async for item in read_file(f):
        p1, p2 = item.strip().split(" ")
        p2_actual = mapping[p2]
        total_score += SCORES[p2_actual] + 1 + await play(SCORES[p1], SCORES[p2_actual])

    return total_score


async def part2(f: str):
    total_score = 0
    async for item in read_file(f):
        play, strategy = item.strip().split(" ")

        if strategy == "X":  # must loose
            total_score += SCORES[await loosing_play(play)] + 1 + LOOSE
        elif strategy == "Y":  # must draw
            total_score += SCORES[play] + 1 + DRAW
        else:  # must win
            total_score += SCORES[await winning_play(play)] + 1 + WIN

    return total_score


async def main(part: str, f: str):
    if part == "2":
        return await part2(f)
    else:
        return await part1(f)