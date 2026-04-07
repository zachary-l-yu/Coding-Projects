# a tool that organises files on my laptop
# started: April 6, 2026 (morning)
# finished: ???

import os
import shutil

downloads_path = '/Users/zacharyyu/Downloads/'

# get all files in the downloads folder
downloads = os.listdir(downloads_path)

# join the new file names into downloads
pdfs = os.path.join(downloads_path, "pdfs")
word_docs = os.path.join(downloads_path, "word-docs")
images = os.path.join(downloads_path, "images")
audio_video = os.path.join(downloads_path, "audio-video")
misc = os.path.join(downloads_path, "misc")

# folder path names
folders = [pdfs, word_docs, images, audio_video, misc]

# make new folders
for folder in folders:
    # only make a new folder if the folder doesn't already exist
    if not os.path.exists(folder):
        os.mkdir(folder)


for download in downloads:
    # create full path of the file
    path = os.path.join(downloads_path, download)

    # it has to be a file, not a folder
    if not os.path.isfile(path):
        continue

    else:

        # add to pdfs
        if download.endswith(".pdf"):
            # create destination path (where it will go)
            destination = os.path.join(pdfs, download)

            # move file using shutil module
            shutil.move(path, destination)

            # tell the user
            print("Moved to PDFs!")

        # add to word documents
        elif download.endswith(".docx"):
            destination = os.path.join(word_docs, download)

            shutil.move(path, destination)

            print("Moved to Word Docs!")

        # add to images
        elif download.endswith(".png") or download.endswith(".jpg") or download.endswith(".png"):
            destination = os.path.join(images, download)

            shutil.move(path, destination)

            print("Moved to images!")

        # add to audio/video
        elif download.endswith(".mp3") or download.endswith(".mp4") or download.endswith(".mov"):
            destination = os.path.join(audio_video, download)

            shutil.move(path, destination)

            print("Moved to audio/video!")

        # add to misc
        else:
            destination = os.path.join(misc, download)

            shutil.move(path, destination)

            print("Moved to misc!")


# success message
print("Successfully organised the Downloads folder!")
