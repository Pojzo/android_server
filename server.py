import asyncio
import logging

logging.basicConfig(level=logging.DEBUG, format='%(name)s:[%(levelname)s]: %(message)s')
logger = logging.getLogger('Server')

HOST = '0.0.0.0'
PORT = 44444
MAX_CLIENTS = 10

class Server:
    def __init__(self, host: str, port: int):
        self.host = host
        self.port = port
        self.loop = asyncio.get_event_loop()

    async def handle_client_receive(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        print("Starting client receive")
        while True:
            data = await reader.read(1024)
            if not data:
                logger.info('Client disconnected')
                break
            logger.info(f'Received: {data.decode()}')

        writer.close() 

    async def handle_client_send(self, writer: asyncio.StreamWriter):
        print("Starting user input")
        while True:
            data = await self.loop.run_in_executor(None, input)

            writer.write((data + '\n').encode())
            print("Sent: ", data)
            await writer.drain()
    
    async def handle_client(self, reader: asyncio.StreamReader, writer: asyncio.StreamWriter):
        logger.info('New client connected')
        receive_task = asyncio.create_task(self.handle_client_receive(reader, writer))
        send_task = asyncio.create_task(self.handle_client_send(writer))
        await asyncio.gather(receive_task, send_task)

    async def listen(self):
        server = await asyncio.start_server(self.handle_client, self.host, self.port)
        async with server:
            await server.serve_forever()

if __name__ == '__main__':
    server = Server(HOST, PORT)
    server.loop.run_until_complete(server.listen())