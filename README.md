# Batch Mux

This script is used to batch append Chapters, fonts and subtitles into the mkvfiles.\
Follows the animetosho attachments download folder structure.\
(Created for anime use)

```
-------Folder Structure-------

root
|
|--append
|  |--attachments_folder_1
|  |  |--attachments
|  |  |  |--font1.ttf
|  |  |  `--font2.ttf
|  |  |
|  |  |--subtitle1.ass
|  |  |--subtitle2.ass
|  |  |
|  |  `--chapters.xml
|  |
|  |--attachments_folder_2
|  |  |--attachments
|  |  |  |--font1.ttf
|  |  |  `--font2.ttf
|  |  |
|  |  |--subtitle1.ass
|  |  |--subtitle2.ass
|  |  |
|  `  `--chapters.xml
|
|--mkvfiles
|  |--mkv1.mkv
|  `--mkv2.mkv
|
|--output (will be created)
|  |--mkvout1.mkv
|  `--mkvout2.mkv
|
`--Batch_Mux.py
```

The above folder structure is to be followed.

# Dependencies

Download the requirements.txt file and run
```
pip install -r requirements.txt
```
or just run
```
pip install pymkv
```

> Make sure mkvmerge has been added to PATH or copy mkvmerge.exe to the root (or parent) folder for the script to detect mkvmerge

# Run

To run the script, open the terminal in the root folder and run
```
python Batch_Mux.py
```

# Links

[pymkv docs](https://pymkv.shel.dev/en/stable/)\
[mkvtoolnix](https://mkvtoolnix.download/downloads.html)\
[python](https://www.python.org/downloads/)