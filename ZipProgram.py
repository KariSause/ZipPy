import zipfile, os
os.chdir("C:\\")
exampleZip = zipfile.ZipFile("OurZipFile.zip")
exampleZip.namelist()
spamInfo = exampleZip.getinfo('Text.txt')
print('Сжатый файл в %s раза меньше!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()
