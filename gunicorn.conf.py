import os


bind = "0.0.0.0:" + os.environ.get("PORT", "8000")

workers = int(os.environ.get("WEB_CONCURRENCY", 2))
threads = int(os.environ.get("PYTHON_THREADS", 4))

timeout = 120
loglevel = "info"