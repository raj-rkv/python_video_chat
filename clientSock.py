import socket ,cv2

def videoClient(ip,port):
    HOST =ip  # The server's hostname or IP address
    PORT=port

    s=socket.socket()
    s.connect((HOST, PORT))

    cap = cv2.VideoCapture(0) 

    while True:
        ret,photo = cap.read()

        cv2.imwrite('clientimg.jpg',photo)

        file = open('clientimg.jpg', 'rb')

        data = file.read(1228800)

        file.close()

        if not (data):
            break

        s.sendall(data)

        file = open('receiveimg.jpg', "wb")

        data = s.recv(1228800)

        if not (data):
            break
        file.write(data)

        file.close()

        photo=cv2.imread('receiveimg.jpg')

        cv2.imshow("client side", photo)

        if cv2.waitKey(10) == 13:
            break

    cv2.destroyAllWindows()
    s.close()


