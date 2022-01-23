from os import listdir, rename, makedirs
from os.path import isfile, join, exists
import subprocess
from tqdm import tqdm

def converter():
    # list of extensions that needs to be ignored
    ignored_extensions = ['pdf', 'txt']

    downloaded_epub = "/Users/jennifersequina/Downloads/"

    mobi_kindle = downloaded_epub + "mobi_kindle/"

    if not exists(mobi_kindle):
        print("Folder - 'mobi_kindle/' - does not exist, making it for you")
        makedirs(mobi_kindle)

    processed_epub = downloaded_epub + "processed_epub/"

    if not exists(processed_epub):
        print("Folder - 'processed_epub/' - does not exist, making it for you")
        makedirs(processed_epub)

    raw_files = [f for f in listdir(downloaded_epub) if isfile(join(downloaded_epub, f))]
    converted_files = [f for f in listdir(mobi_kindle) if isfile(join(mobi_kindle, f))]

    # return file extension. pdf or epub or mobi
    def get_file_extension(f):
        return f.split(".")[-1]

    # return name of file to be kept after conversion
    def get_final_filename(f):
        f = f.split(".")
        filename = ".".join(f[0:-1])
        processed_file_name = filename+".mobi"
        return processed_file_name

    # convert function using calibre ebook-convert
    def convert_files():
        for f in tqdm(raw_files):
            final_file_name = get_final_filename(f)
            extension = get_file_extension(f)
            if final_file_name not in converted_files and extension not in ignored_extensions:
                print("Converting : "+f)
                try:
                    subprocess.call(['/Applications/calibre.app/Contents/MacOS/ebook-convert', downloaded_epub+f, mobi_kindle+final_file_name])
                    s = rename(downloaded_epub+f, processed_epub+f),
                    print(s)
                except Exception as e:
                    print(e)
            else:
                print("Already exists : "+final_file_name)

    if __name__ == "__main__":
        # convert any suitable files not already converted
        source_files = ([f for f in listdir(downloaded_epub) if isfile(join(downloaded_epub, f))])
        if source_files:
            convert_files()
        else:
            print("No files to convert")


converter()