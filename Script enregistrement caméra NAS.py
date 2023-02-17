import cv2 # Chargement de la bibliothèque OpenCV
# rtsp_url = "rtsp://192.168..." # Chemin d'accès à la vidéo en RTSP
# output_path = "..." # Chemin d'enregistrement de la vidéo
# Paramètres du flux vidéo de la caméra
fps = 25.0 # Nombre d'images par seconde
frame_size = (1920, 1080) # Taille de la vidéo (largeur, hauteur) en pixels, à adapter à votre caméra, la caméra que nous utilisons ici est une caméra 1080p.
cap = cv2.VideoCapture(rtsp_url) # Initialisation du flux RTSP
fourcc = cv2.VideoWriter_fourcc(*"mp4") # Codec de la vidéo
out = cv2.VideoWriter(output_path, fourcc, fps, frame_size) # Initialisation de l'enregistreur vidéo
# Ici la boucle infinie qui enregistre la vidéo
while True:
    ret, frame = cap.read()
    if ret: out.write(frame)
    else: break
cap.release() # Fermeture du flux RTSP
out.release() # Fermeture de l'enregistreur vidéo