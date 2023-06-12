import asyncio
import time

clients = []  # 클라이언트 목록
server_address = ('', 2500)

async def client_handler(reader, writer):
    addr = writer.get_extra_info('peername')

    # 새로운 클라이언트이면 목록에 추가
    if (reader, writer, addr) not in clients:
        print('new client', addr)
        clients.append((reader, writer, addr))

    while True:
        data = await reader.read(1024)
        if not data:
            break
        # 'quit'을 수신하면 해당 클라이언트를 목록에서 삭제
        if b'quit' in data:
            if (reader, writer, addr) in clients:
                print(addr, 'exited')
                clients.remove((reader, writer, addr))
                continue
        print(time.asctime() + str(addr) + ':' + data.decode())
        # 모든 클라이언트에게 전송
        for client in clients:
            if client[2] != addr:
                client[1].write(data)

    writer.close()

async def main():
    server = await asyncio.start_server(client_handler, *server_address)

    addr = server.sockets[0].getsockname()
    print('Server Started on', addr)

    async with server:
        await server.serve_forever()

asyncio.run(main())
