from asyncio import futures
from concurrent.futures import ThreadPoolExecutor

from authorisation.auth_pb2_grpc import add_AuthServicer_to_server
from .base import engine, Base
from .service import AuthService
import grpc
from os import environ


def main():
    Base.metadata.create_all(engine)

    server = grpc.server(ThreadPoolExecutor(max_workers=1))

    add_AuthServicer_to_server(AuthService(), server)

    PORT = environ.get('PORT', 9000)

    server.add_insecure_port(f'localhost:{PORT}')
    server.start()

    print(f'Server started on localhost:{PORT}')

    server.wait_for_termination()

if __name__ == '__main__':
    main()