from os import walk
from os.path import splitext, join
from tinytag import TinyTag


def is_mp3_file(file):
    return splitext(file)[1] == '.mp3'


def get_audio_information(path):
    audio = TinyTag.get(path)
    if not audio.duration:
        audio.duration = 0
    return {
        'duration': round(audio.duration),
        'size': audio.filesize
    }


def get_mp3_files(path):
    mp3_files = []
    for root, dirs, files in walk(path):
        for file in files:
            if is_mp3_file(file):
                mp3_path = join(root, file)
                mp3_information = get_audio_information(mp3_path)
                mp3_files.append(
                    {
                        'title': file,
                        'path': mp3_path,
                        **mp3_information
                    }
                )
    return mp3_files
