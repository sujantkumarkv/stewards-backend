import requests, aiohttp, asyncio, os

query_id= 1157736
apiKey= os.environ["DUNE_API_KEY"]
dune_url= f"https://api.dune.com/api/v0/query/{query_id}/results"
async def fetch():

    async with aiohttp.ClientSession() as session:
        async with session.get(dune_url, headers={'X-Dune-API-Key': apiKey}) as response:
            result = await response.json()
            print(result)

loop= asyncio.new_event_loop()
asyncio.set_event_loop(loop) #creating a new event loop & setting it.
#loop = asyncio.get_event_loop()
#loop.run_until_complete(fetchData())


asyncio.run(fetch())

"""
    We need as-of-now a list of query IDs.@#
"""