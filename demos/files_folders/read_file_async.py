import asyncio
import aiofiles


async def read_print_file(file_name: str) -> str:
    async with aiofiles.open(
            file_name, "r", encoding="UTF-8") as the_file:

        async for the_line in the_file:
            print(the_line)


async def main() -> None:
    """ main """

    await asyncio.gather(
        read_print_file("colors.txt"),
        read_print_file("colors2.txt")
    )


asyncio.run(main())
