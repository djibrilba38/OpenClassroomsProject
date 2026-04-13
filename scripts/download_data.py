import urllib.request
import zipfile
import os

url = "https://s3-eu-west-1.amazonaws.com/static.oc-static.com/prod/courses/files/Parcours_data_scientist/Projet+-+Donn%C3%A9es+%C3%A9ducatives/Projet+Python_Dataset_Edstats_csv.zip"

os.makedirs("data", exist_ok=True)

print("⬇️ Downloading data...")
urllib.request.urlretrieve(url, "data/data.zip")

print("📦 Extracting...")
with zipfile.ZipFile("data/data.zip", "r") as zip_ref:
    zip_ref.extractall("data")

os.remove("data/data.zip")

print("✅ Done! Data available in /data")