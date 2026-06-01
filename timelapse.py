import cv2
import os
from natsort import natsorted


def create_timelapse(dirpic, diroutvid, framerate):
    # === CONFIGURATION ===
    dossier_images = dirpic       # Dossier contenant les photos
    video_sortie = diroutvid + "/timelapse.mp4"  # Nom du fichier vidéo final
    fps = framerate                        # Images par seconde

    # Extensions acceptées
    extensions = (".jpg", ".jpeg", ".png")

    # === RÉCUPÉRATION DES IMAGES ===
    images = [
        f for f in os.listdir(dossier_images)
        if f.lower().endswith(extensions)
    ]

    print(images)

    # Tri naturel : image1, image2, image10...
    images = natsorted(images)

    print(images)

    if not images:
        raise Exception("Aucune image trouvée.")

    # === LECTURE DE LA PREMIÈRE IMAGE ===
    premiere_image = cv2.imread(os.path.join(dossier_images, images[0]))

    hauteur, largeur, _ = premiere_image.shape

    # === INITIALISATION VIDÉO ===
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')

    video = cv2.VideoWriter(
        video_sortie,
        fourcc,
        fps,
        (largeur, hauteur)
    )

    # === AJOUT DES IMAGES ===
    for nom_image in images:
        chemin = os.path.join(dossier_images, nom_image)

        image = cv2.imread(chemin)

        # Vérifie que toutes les images ont la même taille
        image = cv2.resize(image, (largeur, hauteur))

        video.write(image)

        print(f"Ajout : {nom_image}")

    # === FINALISATION ===
    video.release()

    print(f"\nTimelapse créé : {video_sortie}")
