def read():
    """
    This coroutine reads data, yields it, and completes when no more data is available.

    Function is a Generator, doesn't return any output. It should be used in a loop where values are sent
    to continue the operation.

    Instructions to Call Function:
        Instantiate a generator object.
        Use generator.send(None) to start the generator.
        Then use generator.send(value) to send value to generator context.

    Example:
    ```
    gen = read()
    gen.send(None)   # To start coroutine
    while data:
        gen.send(data)   # Replace 'data' with real data
    ```

    Note:
    After the last data is sent, generator should be explicitly closed by calling generator.close()
    to avoid 'GeneratorExit' exception.
    """
    try:
        while True:
            data = yield
            print(f"Data: {data}")
    except GeneratorExit:
        print("Reading finished, closing generator.")
