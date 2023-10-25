try:
    server.start()
except ServerCrashError:
    logger.error("Server crashed, restarting...")
    server.restart()
else:
    logger.info("Server started successfully")
