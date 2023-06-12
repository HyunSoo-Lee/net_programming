import asyncio
import random

BUF_SIZE = 1024
LENGTH = 4  # '파일 크기': 4바이트

async def handle_client(reader, writer):
    addr = writer.get_extra_info('peername')
    num = await reader.read(BUF_SIZE)  # 넘버 메시지 수신

    if not num:
        writer.close()
        return
    else:
        num = int.from_bytes(num, 'big')
        print('client:', addr, num)

    temp = 0
    humi = 0
    result = ''

    if num == 1:
        temp = random.randint(0, 40)
        result = f'Temp={temp}'
        writer.write(result.encode())
    elif num == 2:
        humi = random.randint(0, 100)
        result = f'Humi={humi}'
        writer.write(result.encode())

    print('sended : ', result)

    await writer.drain()
    writer.close()

async def main():
    server = await asyncio.start_server(handle_client, 'localhost', 9999)

    print('Device1 server is running...')

    async with server:
        await server.serve_forever()

asyncio.run(main())
