import asyncio

async def primer_async(tiempo):
    print(f"Hola {tiempo}")
    await asyncio.sleep(tiempo)
    print(f"Adios {tiempo}")


async def corutinas():
    return await asyncio.gather(primer_async(5), primer_async(3))

loop = asyncio.get_event_loop()
loop.run_until_complete(corutinas())

asyncio.run(primer_async(5))
asyncio.run(primer_async(3))