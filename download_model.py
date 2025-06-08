import os
import gdown
import zipfile

def download_model():
    model_folder = "bert_model_final"
    if not os.path.exists(model_folder):
        url = "https://drive.google.com/uc?id=1O5Z2moYiT0ji-YbviEXgVUEa0ahF9YFa"
        output = "bert_model_final.zip"
        gdown.download(url, output, quiet=False)

        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall(".")  # Extrait les fichiers au bon endroit
        os.remove(output)
    else:
        print(f"Le dossier {model_folder} existe déjà.")

download_model()
