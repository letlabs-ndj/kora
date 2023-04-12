import rtsp

client = rtsp.Client(rtsp_server_uri="rtsp://admin:brandon@1@192.168.1.108")
client.read().show()
client.close()
