import zipfile
import shutil

# par défaut stock sans compresser
"""fichier_zip = zipfile.ZipFile("fichier_excel.zip", 'w', zipfile.ZIP_DEFLATED)
fichier_zip.write("octobre.xlsx")
fichier_zip.write("novembre.xlsx")
fichier_zip.write("decembre.xlsx")
fichier_zip.close()"""

# compresser les dossiers en zip
shutil.make_archive("fichier_excel2", "zip", "automatisation")

# extraire les dossiers zip
#shutil.unpack_archive("fichier_excel2.zip", "automatisation", "zip")