"""Tentative to get code from images."""
from glob import glob
import pytesseract
from PIL import Image, ImageOps


def enlarge_image() -> None:
    size = (9000, 12000)

    images = glob("../../Images/*.jpg")
    for image in images:
        im = image.split("/")
        fic = im[-1]
        fic_items = fic.split(".")

        with Image.open(image) as img:
            ImageOps.cover(img, size).save("/".join(im[:-1]) + "/x3/" + fic_items[0] + "_x3." + fic_items[1])


def get_text_in_image() -> None:
    """

    Options Tesseract OCR
    OCR Engine Mode : moteur de reconnaissance de caractères
    OEM Signification
    0   Ancien moteur Tesseract (legacy)
    1   Réseau neuronal LSTM uniquement
    2   Legacy + LST
    3   Choix automatique (par défaut)

    Page Segmentation Mode : mode de segmentation de la page
    PSM Hypothèse
    3   Page complète (défaut)
    4   Une seule colonne
    6   Un bloc uniforme de texte
    7   Une seule ligne
    8   Un seul mot
    10  Un seul caractère
    11  Texte dispersé
    13  Ligne brute (raw line)
    """
    result = "resultat.txt"
    f = open(file=result, mode="w", buffering=1, encoding="utf-8")

    images = glob("../../Images/*.jpg")
    # -c preserve_interword_spaces=1
    custom_config = r"--oem 3 --psm 6"
    for image in images:
        with Image.open(image) as im:
            # gray = im.convert("L")
            text = pytesseract.image_to_string(im,
                                               lang="fra",
                                               config=custom_config
                                               )
            f.write(text)
            # f.write("-" * 90)
    f.close()


def main() -> None:
    get_text_in_image()


if __name__ == "__main__":
    main()
