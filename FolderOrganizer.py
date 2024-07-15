import os
import shutil

image_extensions = {"3dm",".3ds",".max",".avif",".bmp",".dds",".gif",".heic",".heif",".jpg",".jpeg",".jxl",
                    ".png",".psd",".xcf",".tga",".thm",".tif",".tiff",".yuv",".ai",".eps",".ps",".svg",".dwg",".dxf",".gpx",".kml",".kmz",".webp"}

video_extensions = {"3g2","3gp","aaf","asf","avchd","avi","car","dav","drc","flv","m2v","m2ts","m4p","m4v",
                    "mkv","mng","mov","mp2","mp4","mpe","mpeg","mpg","mpv","mts","mxf","nsv","ogv","ogm","ogx","qt","rm","rmvb","roq","srt","svi","vob","webm","wmv","xba","yuv"}

audio_extensions = {".aac",".aiff",".ape",".au",".flac",".gsm",".it",".m3u",".m4a",".mid",".mod",".mp3",".mpa",".ogg",".pls",".ra",".s3m",".sid",".wav",".wma",".xm"}

archive_extensions = {".7z",".a",".aar",".apk",".ar",".bz2",".br",".cab",".cpio",".deb",".dmg",".egg",".gz",".iso",".jar",".lha",
                      ".lz",".lz4",".lzma",".lzo",".mar",".pea",".rar",".rpm",".s7z",".shar",".tar",".tbz2",".tgz",".tlz",".txz",
                      ".war",".whl",".xpi",".zip",".zipx",".zst",".xz",".pak"}

document_extensions = {".pdf",".doc",".xls",".xlsx",".ods"}

source_dir = 'D:/Downloads/'

if not os.path.isdir(source_dir):
    source_dir = input("Enter the directory path:\n")

images_dir = os.path.join(source_dir, 'Images/')
video_dir = os.path.join(source_dir, 'Video/')
audio_dir = os.path.join(source_dir, 'Audio/')
archive_dir = os.path.join(source_dir, 'Archive/')
documents_dir = os.path.join(source_dir, 'Documents/')
executables_dir = os.path.join(source_dir, 'Executables/')
others_dir = os.path.join(source_dir, 'Others/')

if not os.path.isdir(images_dir):
    os.mkdir(images_dir)
if not os.path.isdir(video_dir):
    os.mkdir(video_dir)
if not os.path.isdir(audio_dir):
    os.mkdir(audio_dir)
if not os.path.isdir(archive_dir):
    os.mkdir(archive_dir)
if not os.path.isdir(documents_dir):
    os.mkdir(documents_dir)
if not os.path.isdir(executables_dir):
    os.mkdir(executables_dir)
if not os.path.isdir(others_dir):
    os.mkdir(others_dir)



for file in os.listdir(source_dir):
    if os.path.isdir(os.path.join(source_dir,file)):
        continue
    else:
        shutil.move(os.path.join(source_dir,file),os.path.join(others_dir,file))

    for extension in image_extensions:
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir,file),os.path.join(images_dir,file))
            break

    for extension in video_extensions:
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir,file),os.path.join(video_dir,file))
            break

    for extension in audio_extensions:
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir,file),os.path.join(audio_dir,file))
            break

    for extension in archive_extensions:
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir,file),os.path.join(archive_dir,file))
            break
    for extension in document_extensions:
        if file.endswith(extension):
            shutil.move(os.path.join(source_dir,file),os.path.join(documents_dir,file))
            break

    if file.endswith('.exe'):
        shutil.move(os.path.join(source_dir,file),os.path.join(executables_dir,file))
    
    