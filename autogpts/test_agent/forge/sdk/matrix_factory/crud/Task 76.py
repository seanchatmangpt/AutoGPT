try:
    server.start()
except ServerCrashError as e:
    logger.error(f"Server crashed: {e}")
    sys.exit(1)
