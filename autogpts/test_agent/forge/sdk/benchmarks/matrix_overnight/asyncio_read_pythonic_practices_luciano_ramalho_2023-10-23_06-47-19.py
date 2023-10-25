import asyncio


async def read():
    """
    An example of coroutine that is following the Pythonic practices advocated by Luciano Ramalho in the book "Fluent Python".
    This function reads from an asyncio stream. Since asyncio operations are cooperative, the code does not block the global
    interpreter lock (GIL), allowing other operations to continue when this function awaits on IO.

    This function does not accept any argument and does not return a specific output.

    Postcondition: For this coroutine, the post-condition can include ensuring that the data has been read from
    the stream before calling any operations that rely on that data.
    """
    reader, _ = await asyncio.open_connection("127.0.0.1", 8888)
    data = await reader.read(100)
    print(f"Received: {data.decode()!r}")
