import os
import gdown
import zipfile

def download_model():
    model_folder = "bert_model_final"
    if not os.path.exists(model_folder):
        os.makedirs(model_folder, exist_ok=True)
        url = "https://drive.google.com/file/d/1O5Z2moYiT0ji-YbviEXgVUEa0ahF9YFa/view?usp=sharing"
        output = "bert_model_final.zip"
        gdown.download(url, output, quiet=False)

        with zipfile.ZipFile(output, 'r') as zip_ref:
            zip_ref.extractall(model_folder)
        os.remove(output)
    else:
        print(f"Le dossier {model_folder} existe déjà.")

download_model()
