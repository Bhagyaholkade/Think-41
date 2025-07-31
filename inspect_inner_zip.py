import zipfile

nested_zip = 'ecommerce-dataset-main/archive.zip'

print("📁 Inspecting contents of archive.zip...\n")
with zipfile.ZipFile(nested_zip, 'r') as zip_ref:
    for file in zip_ref.namelist():
        print(" -", file)
