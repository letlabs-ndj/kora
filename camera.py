# import cv2

# capture = cv2.VideoCapture("http://192.168.1.108:80/videostream.cgi?user=admin&pwd=brandon@1")
# # Configuration des paramètres de la caméra
# capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
# capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
# capture.set(cv2.CAP_PROP_FPS, 30)

# # Capture d'une image
# ret, frame = capture.read()

# # Enregistrement de l'image au format PNG
# if ret:
#     cv2.imwrite('image.png', frame)
#     print('Image enregistrée avec succès.')
# else:
#     print('Erreur lors de la capture de l\'image.')

# # Libération des ressources
# capture.release()
# cv2.destroyAllWindows()
"""Access IP Camera in Python OpenCV"""

import cv2

# Adresse IP de votre caméra
camera_ip = 'http://admin:brandon@1@192.168.1.108:80'

# Connexion à la caméra
capture = cv2.VideoCapture(camera_ip)

# Configuration des paramètres de la caméra
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 1280)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 720)
capture.set(cv2.CAP_PROP_FPS, 30)

# Capture d'une image
ret, frame = capture.read()

# Enregistrement de l'image au format PNG
if ret:
    cv2.imwrite('image.png', frame)
    print('Image enregistrée avec succès.')
else:
    print('Erreur lors de la capture de l\'image.')

# Libération des ressources
capture.release()
cv2.destroyAllWindows()