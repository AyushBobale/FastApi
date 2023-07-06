from motor.motor_asyncio import AsyncIOMotorClient

conn = {}


async def ping_server(uri):
    global conn
    client = AsyncIOMotorClient(uri)
    db = client.analystai
    try:
        client.admin.command("ping")
        print("Pinged your deployment. You successfully connected to MongoDB!")
        conn = {"client": client, "db": db}
        return {"client": client, "db": db}
    except Exception as e:
        print(e)
        exit()
