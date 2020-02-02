from lib import LightShot
from os import path
import os
import asyncio
import click


async def run(folder_name: str):
    while True:
        await LightShot.save(await LightShot.get_image(), folder_name)


@click.command()
@click.option("--tasks", default=5, help="Count of asynchronous tasks.")
@click.option("--folder", default="images", help="Path where images will be saved.")
def main(tasks: int, folder: str):
    if not path.exists(folder):
        os.mkdir(folder)

    loop = asyncio.get_event_loop()
    for i in range(tasks):
        loop.create_task(run(folder))
    loop.run_forever()


if __name__ == '__main__':
    main()
