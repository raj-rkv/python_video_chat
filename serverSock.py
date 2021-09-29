import socket ,cv2

def serverVideo(ip,port):
    HOST =ip # Standard loopback interface address (localhost)
    PORT=port

    s=socket.socket()

    s.bind((HOST, PORT))

    s.listen()

    conn, addr = s.accept()

    print('Connected by', addr) 

    cap = cv2.VideoCapture(0) # check this

    while True:

        file = open('srimg.jpg', "wb")

        data = conn.recv(122880)

        if not (data):

            break

        file.write(data)

        file.close()


        photo=cv2.imread('srimg.jpg')

        cv2.imshow("server side", photo)

        if cv2.waitKey(10) == 13:

            break


        ret, photo = cap.read()

        cv2.imwrite('ssimg.jpg',photo)

        file = open('ssimg.jpg', 'rb')

        data = file.read(122880)

        if not (data):

            break

        conn.sendall(data)

        file.close()


    conn.close()
    cv2.destroyAllWindows()
    s.close()
