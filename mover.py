import os
import shutil
import sys
from datetime import datetime
from pathlib import Path

from PIL import Image
from PIL.ExifTags import TAGS

if len(sys.argv) != 3:
    print(
        "Pass only two arguments, the path to the Photos-001 file and the path to the destination folder"
    )

if os.path.isdir(sys.argv[1]):
    files = os.listdir(sys.argv[1])
    for file in files:
        if os.path.isfile(os.path.join(sys.argv[1], file)):
            img = Image.open(os.path.join(sys.argv[1], file))
            exifdata = img.getexif()
            dat = exifdata.get(306)
            date = datetime.strptime(dat, "%Y:%m:%d %H:%M:%S")
            if Path(os.path.join(sys.argv[2], str(date.year))).exists() == False:
                os.makedirs(os.path.join(sys.argv[2], str(date.year)))
            month = date.strftime("%B")
            if Path(os.path.join(sys.argv[2], str(date.year), month)).exists() == False:
                os.makedirs(os.path.join(sys.argv[2], str(date.year), month))
            if (
                Path(
                    os.path.join(sys.argv[2], str(date.year), month, str(date.day))
                ).exists()
                == False
            ):
                os.makedirs(os.path.join(sys.argv[2], str(date.year), month, str(date.day)))
            shutil.copy(
                os.path.join(sys.argv[1], file),
                os.path.join(sys.argv[2], str(date.year), month, str(date.day)),
            )
