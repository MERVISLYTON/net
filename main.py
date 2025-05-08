import asyncio

async def handle_connection(reader, writer):
    data = await reader.read(1024)
    request = data.decode()
    
    first_line = request.split('\r\n')[0]
    parts = first_line.split()
    if not parts:
        writer.close()
        return
    
    method, path = parts[0], parts[1]
    
    if method == 'GET':
        if path == '/':
            try:
                with open('templates/index.html', 'rb') as f:
                    content = f.read()
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    b"Content-Type: text/html\r\n\r\n" + 
                    content
                )
            except:
                response = b"HTTP/1.1 404 Not Found\r\n\rNo page found"
        
        elif path == '/register':
            try:
                with open('templates/register.html', 'rb') as f:
                    content = f.read()
                response = (
                    b"HTTP/1.1 200 OK\r\n"
                    b"Content-Type: text/html\r\n\r\n" + 
                    content
                )
            except:
                response = b"HTTP/1.1 404 Not Found\r\n\rNo page found"
        
        else:
            response = b"HTTP/1.1 404 Not Found\r\n\rInvalid path"
    
    elif method == 'POST' and path == '/submit':
        body = request.split('\r\n\r\n')[1]
        fields = body.split('&')
        user_data = {}
        
        for field in fields:
            key, value = field.split('=')
            user_data[key] = value
        
        if 'username' in user_data and 'email' in user_data:
            with open('db.txt', 'a') as f:
                f.write(f"{user_data['username']} {user_data['email']}\n")
            response = b"HTTP/1.1 303 See Other\r\nLocation: /\r\n\r\n"
        else:
            response = b"HTTP/1.1 400 Bad Request\r\n\rMissing fields"
    
    else:
        response = b"HTTP/1.1 405 Not Allowed\r\n\rBad method"
    
    writer.write(response)
    await writer.drain()
    writer.close()

async def run_server():
    server = await asyncio.start_server(handle_connection, 'localhost', 8085)
    print('Server running...')
    
    async with server:
        await server.serve_forever()

if __name__ == '__main__':
    asyncio.run(run_server())