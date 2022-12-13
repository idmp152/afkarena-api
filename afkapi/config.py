from typing import Union
from os import PathLike

# TODO: Move either to .env file or to .yaml file

# Database connection string relative to the messenger.core module
DB_CONNECTION_STRING: str = "sqlite+aiosqlite:////home/overwrite/Documents/CodingProjects/AFKBeta/afkbeta/db.sqlite3"

# SSL key and certificate file paths relative to the messenger.main module
SSL_KEYFILE_PATH: Union[str, PathLike] = "..\\certs\\key.pem"
SSL_CERTFILE_PATH: Union[str, PathLike] = "..\\certs\\cert.pem"

# Host and port for the Uvicorn ASGI server
HOST: str = "0.0.0.0"
PORT: int = 8080
