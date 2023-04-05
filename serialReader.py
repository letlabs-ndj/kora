import serial

while True:
    # Ouvrir la connexion série avec la Raspberry Pi
    ser = serial.Serial('/dev/ttyACM0', 9600)

    # Lire la donnée reçue depuis la Raspberry Pi
    data = ser.readline().decode().strip()
    print(data)
    # Fermer la connexion série
    ser.close()

    # Stocker les données dans un fichier texte
    with open('donnees.txt', 'w') as file:
        file.write(str(data))
