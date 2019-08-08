import asyncio
from time import sleep

with open('barcodes.txt', 'r') as f:
    args = f.read().splitlines()

def lineEnd(arg):
    switcher = {
        '0': "",
        '1': "\r",
        '2': "\r\n",
    }
    return switcher[arg]


async def handle(reader, writer):
    addr = writer.get_extra_info('peername')
    message = f"{addr!r} is connected !!!!"
    print(message)

    for x in range(len(args)):
        if x != 0:
            sleep(5)
            barcode = args[x] + lineEnd(args[0])
            b = barcode.encode('utf-8')
            writer.write(b)
            print(b)

async def main():
    server = await asyncio.start_server(
        handle, '127.0.0.1', 8889)
    addr = server.sockets[0].getsockname()
    print(f'Serving on {addr}')
    async with server:
        await server.serve_forever()

asyncio.run(main())

# for x in range(len(args)):
#     if x != 0:
#         sleep(5)
#         print(args[x] + lineEnd(args[0]))

# input('EXIT')