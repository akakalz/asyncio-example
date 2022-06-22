import asyncio
import requests


async def simple_api_call() -> requests.Response:
    resp = requests.get("http://restapi.adequateshop.com/api/Traveler/")
    return resp


async def simple_io_call() -> str:
    with open("./src/example_brd.md", "r") as read_file:
        return read_file.read()


async def main() -> None:
    resp, brd = await asyncio.gather(
        simple_api_call(),
        simple_io_call(),
    )
    print(resp.text)
    print(brd)


if __name__ == "__main__":
    asyncio.run(main())