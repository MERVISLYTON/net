import asyncio
import hashlib
async def handle_client(reader, writer):
    client_addr = writer.get_extra_info('peername')


    try:
        message = await reader.read(100)
        
        hashed_client_address = hashlib.sha1(client_addr[0].encode()).hexdigest()
        print(f"{hashed_client_address[:8]} : {message.decode("utf-8")}")
        writer.write(message)
        await writer.drain()
            
    except Exception as error:
        print("")
    finally:
        writer.close()
        await writer.wait_closed()
    

async def main():
    
    tcp_server = await asyncio.start_server(handle_client, "127.0.0.1", 300)
    addr = tcp_server.sockets[0].getsockname()
    print(f"This  Messaging coordinator server sockect: {addr}")

    async with tcp_server:
        await tcp_server.serve_forever() 


if __name__ == "__main__":
    asyncio.run(main())