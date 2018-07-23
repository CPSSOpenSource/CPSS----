import zipfile
import os

if __name__ == "__main__":
  zip = zipfile.Zipfile("cpss_ppt.zip", 'w')
  zip.write(os.path.join(folder, file), file, compress_type = zipfile.ZIP_DEFLATED)
  for folder, subfolders, files in os.walk('./python'):
    zip.write(files, compress_type = zipfile.ZIP_DEFLATED)
  zip.close()
