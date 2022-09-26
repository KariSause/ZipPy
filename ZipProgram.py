import zipfile, os
os.chdir("C:\\Users\\PIV\\Desktop\\Scripts")
exampleZip = zipfile.ZipFile("CatZip.zip")
exampleZip.namelist()
spamInfo = exampleZip.getinfo('Kitty.txt')
print('Сжатый файл в %s раза меньше!' % (round(spamInfo.file_size / spamInfo.compress_size, 2)))
exampleZip.close()