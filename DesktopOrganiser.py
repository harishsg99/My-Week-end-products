from watchdog.observers import Observer
import time
from watchdog.events import FileSystemEventHandler
import os 
import json
import shutil
from datetime import datetime
from time import gmtime, strftime
class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        for filename in os.listdir(folder_to_track):
            i = 1
            if filename != 'AK':
                # try:
                    new_name = filename
                    extension = 'noname'
                    try:
                        extension = str(os.path.splitext(folder_to_track + '/' + filename)[1])
                        path = extensions_folders[extension]
                    except Exception:
                        extension = 'noname'

                    now = datetime.now()
                    year = now.strftime("%Y")
                    month = now.strftime("%m")

                    folder_destination_path = extensions_folders[extension]
                    
                    year_exists = False
                    month_exists = False
                    for folder_name in os.listdir(extensions_folders[extension]):
                        if folder_name == year:
                            folder_destination_path = extensions_folders[extension] + "/" +year
                            year_exists = True
                            for folder_month in os.listdir(folder_destination_path):
                                if month == folder_month:
                                    folder_destination_path = extensions_folders[extension] + "/" + year + "/" + month
                                    month_exists = True
                    if not year_exists:
                        os.mkdir(extensions_folders[extension] + "/" + year)
                        folder_destination_path = extensions_folders[extension] + "/" + year
                    if not month_exists:
                        os.mkdir(folder_destination_path + "/" + month)
                        folder_destination_path = folder_destination_path + "/" + month


                    file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    while file_exists:
                        i += 1
                        new_name = os.path.splitext(folder_to_track + '/' + filename)[0] + str(i) + os.path.splitext(folder_to_track + '/' + filename)[1]
                        new_name = new_name.split("/")[4]
                        file_exists = os.path.isfile(folder_destination_path + "/" + new_name)
                    src = folder_to_track + "/" + filename

                    new_name = folder_destination_path + "/" + new_name
                    os.rename(src, new_name)
                # except Exception:
                #     print(filename)
                #Add the folder path & also create all the folders

extensions_folders = {
#No name
    'noname' : "C:/Users/Harish/Desktop/AK/Other/Uncategorized",
#Audio
    '.aif' : "C:/Users/Harish/Desktop/AK/Audio",
    '.cda' : "C:/Users/Harish/Desktop/AK/Audio",
    '.mid' : "C:/Users/Harish/Desktop/AK/Audio",
    '.midi' : "C:/Users/Harish/Desktop/AK/Audio",
    '.mp3' : "C:/Users/Harish/Desktop/AK/Audio",
    '.mpa' : "C:/Users/Harish/Desktop/AK/Audio",
    '.ogg' : "C:/Users/Harish/Desktop/AK/Audio",
    '.wav' : "C:/Users/Harish/Desktop/AK/Audio",
    '.wma' : "C:/Users/Harish/Desktop/AK/Audio",
    '.wpl' : "C:/Users/Harish/Desktop/AK/Audio",
    '.m3u' : "C:/Users/Harish/Desktop/AK/Audio",
#Text
    '.txt' : "C:/Users/Harish/Desktop/AK/Text/TextFiles",
    '.doc' : "C:/Users/Harish/Desktop/AK/Text/Microsoft/Word",
    '.docx' : "C:/Users/Harish/Desktop/AK/Text/Microsoft/Word",
    '.odt ' : "C:/Users/Harish/Desktop/AK/Text/TextFiles",
    '.pdf': "C:/Users/Harish/Desktop/AK/Text/PDF",
    '.rtf': "C:/Users/Harish/Desktop/AK/Text/TextFiles",
    '.tex': "C:/Users/Harish/Desktop/AK/Text/TextFiles",
    '.wks ': "C:/Users/Harish/Desktop/AK/Text/TextFiles",
    '.wps': "C:/Users/Harish/Desktop/AK/Text/TextFiles",
    '.wpd': "C:/Users/Harish/Desktop/AK/Text/TextFiles",
#Video
    '.3g2': "C:/Users/Harish/Desktop/AK/Video",
    '.3gp': "C:/Users/Harish/Desktop/AK/Video",
    '.avi': "C:/Users/Harish/Desktop/AK/Video",
    '.flv': "C:/Users/Harish/Desktop/AK/Video",
    '.h264': "C:/Users/Harish/Desktop/AK/Video",
    '.m4v': "C:/Users/Harish/Desktop/AK/Video",
    '.mkv': "C:/Users/Harish/Desktop/AK/Video",
    '.mov': "C:/Users/Harish/Desktop/AK/Video",
    '.mp4': "C:/Users/Harish/Desktop/AK/Video",
    '.mpg': "C:/Users/Harish/Desktop/AK/Video",
    '.mpeg': "C:/Users/Harish/Desktop/AK/Video",
    '.rm': "C:/Users/Harish/Desktop/AK/Video",
    '.swf': "C:/Users/Harish/Desktop/AK/Video",
    '.vob': "C:/Users/Harish/Desktop/AK/Video",
    '.wmv': "C:/Users/Harish/Desktop/AK/Video",
#Images
    '.ai': "C:/Users/Harish/Desktop/AK/Images",
    '.bmp': "C:/Users/Harish/Desktop/AK/Images",
    '.gif': "C:/Users/Harish/Desktop/AK/Images",
    '.ico': "C:/Users/Harish/Desktop/AK/Images",
    '.jpg': "C:/Users/Harish/Desktop/AK/Images",
    '.jpeg': "C:/Users/Harish/Desktop/AK/Images",
    '.png': "C:/Users/Harish/Desktop/AK/Images",
    '.ps': "C:/Users/Harish/Desktop/AK/Images",
    '.psd': "C:/Users/Harish/Desktop/AK/Images",
    '.svg': "C:/Users/Harish/Desktop/AK/Images",
    '.tif': "C:/Users/Harish/Desktop/AK/Images",
    '.tiff': "C:/Users/Harish/Desktop/AK/Images",
    '.CR2': "C:/Users/Harish/Desktop/AK/Images",
#Internet
    '.asp': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.aspx': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.cer': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.cfm': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.cgi': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.pl': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.css': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.htm': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.js': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.jsp': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.part': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.php': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.rss': "C:/Users/Harish/Desktop/AK/Other/Internet",
    '.xhtml': "C:/Users/Harish/Desktop/AK/Other/Internet",
#Compressed
    '.7z': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.arj': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.deb': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.pkg': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.rar': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.rpm': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.tar.gz': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.z': "C:/Users/Harish/Desktop/AK/Other/Compressed",
    '.zip': "C:/Users/Harish/Desktop/AK/Other/Compressed",
#Disc
    '.bin': "C:/Users/Harish/Desktop/AK/Other/Disc",
    '.dmg': "C:/Users/Harish/Desktop/AK/Other/Disc",
    '.iso': "C:/Users/Harish/Desktop/AK/Other/Disc",
    '.toast': "C:/Users/Harish/Desktop/AK/Other/Disc",
    '.vcd': "C:/Users/Harish/Desktop/AK/Other/Disc",
#Data
    '.csv': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.dat': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.db': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.dbf': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.log': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.mdb': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.sav': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.sql': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.tar': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.xml': "C:/Users/Harish/Desktop/AK/Programming/Database",
    '.json': "C:/Users/Harish/Desktop/AK/Programming/Database",
#Executables
    '.apk': "C:/Users/Harish/Desktop/AK/Other/Executables",
    '.bat': "C:/Users/Harish/Desktop/AK/Other/Executables",
    '.com': "C:/Users/Harish/Desktop/AK/Other/Executables",
    '.exe': "C:/Users/Harish/Desktop/AK/Other/Executables",
    '.gadget': "C:/Users/Harish/Desktop/AK/Other/Executables",
    '.jar': "C:/Users/Harish/Desktop/AK/Other/Executables",
    '.wsf': "C:/Users/Harish/Desktop/AK/Other/Executables",
#Fonts
    '.fnt': "C:/Users/Harish/Desktop/AK/Other/Fonts",
    '.fon': "C:/Users/Harish/Desktop/AK/Other/Fonts",
    '.otf': "C:/Users/Harish/Desktop/AK/Other/Fonts",
    '.ttf': "C:/Users/Harish/Desktop/AK/Other/Fonts",
#Presentations
    '.key': "C:/Users/Harish/Desktop/AK/Text/Presentations",
    '.odp': "C:/Users/Harish/Desktop/AK/Text/Presentations",
    '.pps': "C:/Users/Harish/Desktop/AK/Text/Presentations",
    '.ppt': "C:/Users/Harish/Desktop/AK/Text/Presentations",
    '.pptx': "C:/Users/Harish/Desktop/AK/Text/Presentations",
#Programming
    '.c': "C:/Users/Harish/Desktop/AK/Programming/C&C++",
    '.class': "C:/Users/Harish/Desktop/AK/Programming/Java",
    '.dart': "C:/Users/Harish/Desktop/AK/Programming/Dart",
    '.py': "C:/Users/Harish/Desktop/AK/Programming/Python",
    '.sh': "C:/Users/Harish/Desktop/AK/Programming/Shell",
    '.swift': "C:/Users/Harish/Desktop/AK/Programming/Swift",
    '.html': "C:/Users/Harish/Desktop/AK/Programming/C&C++",
    '.h': "C:/Users/Harish/Desktop/AK/Programming/C&C++",
#Spreadsheets
    '.ods' : "C:/Users/Harish/Desktop/AK/Text/Microsoft/Excel",
    '.xlr' : "C:/Users/Harish/Desktop/AK/Text/Microsoft/Excel",
    '.xls' : "C:/Users/Harish/Desktop/AK/Text/Microsoft/Excel",
    '.xlsx' : "C:/Users/Harish/Desktop/AK/Text/Microsoft/Excel",
#System
    '.bak' : "C:/Users/Harish/Desktop/AK/System",
    '.cab' : "C:/Users/Harish/Desktop/AK/System",
    '.cfg' : "C:/Users/Harish/Desktop/AK/System",
    '.cpl' : "C:/Users/Harish/Desktop/AK/System",
    '.cur' : "C:/Users/Harish/Desktop/AK/System",
    '.dll' : "C:/Users/Harish/Desktop/AK/System",
    '.dmp' : "C:/Users/Harish/Desktop/AK/System",
    '.drv' : "C:/Users/Harish/Desktop/AK/System",
    '.icns' : "C:/Users/Harish/Desktop/AK/System",
    '.ico' : "C:/Users/Harish/Desktop/AK/System",
    '.ini' : "C:/Users/Harish/Desktop/AK/System",
    '.lnk' : "C:/Users/Harish/Desktop/AK/System",
    '.msi' : "C:/Users/Harish/Desktop/AK/System",
    '.sys' : "C:/Users/Harish/Desktop/AK/System",
    '.tmp' : "C:/Users/Harish/Desktop/AK/System",
}

folder_to_track = 'C:/Users/Harish/Desktop'
folder_destination = 'C:/Users/Harish/Desktop/AK'
event_handler = MyHandler()
observer = Observer()
observer.schedule(event_handler, folder_to_track, recursive=True)
observer.start()

try:
    while True:           
        time.sleep(10)
except KeyboardInterrupt:
    observer.stop()
observer.join()
