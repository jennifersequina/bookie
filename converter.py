from os import listdir, rename
from os.path import isfile, join
import subprocess
from tqdm import tqdm

'''
If variables are used only in one function, lets define them inside the function
'''

'''
This probably can be removed after changing logic of converted 
'''

'''
Functions should not be defined inside other function
'''


'''
Patrick's note:
We want converter to only convert selected file, and return the name of the converted file
'''

def converter() -> str:

    ignored_extensions = ['pdf', 'txt']
    downloaded_epub = "/Users/jennifersequina/Downloads/"
    mobi_kindle = downloaded_epub + "mobi_kindle/"
    processed_epub = downloaded_epub + "processed_epub/"

    raw_files = [f for f in listdir(downloaded_epub) if isfile(join(downloaded_epub, f))]
    converted_files = [f for f in listdir(mobi_kindle) if isfile(join(mobi_kindle, f))]

    def get_file_extension(f):
        return f.split(".")[-1]

    def get_final_filename(f):
        f = f.split(".")
        filename = ".".join(f[0:-1])
        processed_file_name = filename + ".mobi"
        return processed_file_name

    for f in tqdm(raw_files):
        final_file_name = get_final_filename(f)
        extension = get_file_extension(f)
        if final_file_name not in converted_files and extension not in ignored_extensions:
            print("Converting : "+f)
            try:
                subprocess.call(['/Applications/calibre.app/Contents/MacOS/ebook-convert', downloaded_epub+f, mobi_kindle+final_file_name])
                rename(downloaded_epub+f, processed_epub+f)
            except Exception as e:
                print(e)
        else:
            print("Already exists : "+final_file_name)

        print("Kindle Path: " + str(mobi_kindle+final_file_name))
        return str(mobi_kindle+final_file_name)

