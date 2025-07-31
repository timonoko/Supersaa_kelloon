import socket,saa2
           
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(('', 9093))
s.listen(5)
    
while True:
        s.settimeout(0.5)
        try:
            conn, addr = s.accept()
            request = conn.recv(1024)
            request = str(request)
            conn.send(b'HTTP/1.1 200 OK\n')
            conn.send(b'Content-Type: text/html\n')
            conn.send(b'Connection: close\n\n')
            if request.find('/saa') == 6:
                conn.sendall(saa2.indeksi())
            conn.close()
        except OSError:
            pass

