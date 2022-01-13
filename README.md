# Batch Mux

This script is used to batch append Chapters, fonts and subtitles into the mkvfiles.\
Follows the animetosho attachments download folder structure.\
(Created for anime use)

```
-------Folder Structure-------

.
├── append
│   ├── [BlurayDesuYo] Shingeki no Kyojin (The Final Season) - 60 (BD 1920x1080 x265 10bit FLAC) [F97B223C].mkv
│   │   ├── attachments
│   │   │   ├── AGARAMONDPRO-REGULAR.OTF
│   │   │   ├── ANGIE-BOLDITALIC.TTF
│   │   │   ├── ANGIE-BOLD.TTF
│   │   │   ├── BSOD.TTF
│   │   │   ├── CLEARFACESSIBOLD.TTF
│   │   │   ├── GAR-A-MONDTALL-LIGHT.TTF
│   │   │   └── KINESISSTD-BLACKITALIC.OTF
│   │   ├── chapters.xml
│   │   ├── tags.xml
│   │   └── track3_eng.ass
│   └── [BlurayDesuYo] Shingeki no Kyojin (The Final Season) - 61 (BD 1920x1080 x265 10bit FLAC) [93A2A975].mkv
│       ├── attachments
│       │   ├── AGARAMONDPRO-REGULAR.OTF
│       │   ├── ANGIE-BOLDITALIC.TTF
│       │   ├── ANGIE-BOLD.TTF
│       │   ├── BSOD.TTF
│       │   ├── CLEARFACESSIBOLD.TTF
│       │   ├── GAR-A-MONDTALL-LIGHT.TTF
│       │   └── KINESISSTD-BLACKITALIC.OTF
│       ├── chapters.xml
│       ├── tags.xml
│       └── track3_eng.ass
├── mkvfiles
│   ├── [Kawaiika-Raws] Shingeki no Kyojin (2020) 01 [BDRip 1920x1080 HEVC FLAC].mkv [CDBF88C6]
│   └── [Kawaiika-Raws] Shingeki no Kyojin (2020) 02 [BDRip 1920x1080 HEVC FLAC].mkv [42248FF4]
├── output (will be created)
│    ├── [Kawaiika-Raws] Shingeki no Kyojin (2020) 01 [BDRip 1920x1080 HEVC FLAC].mkv [E5B40389]
│    └── [Kawaiika-Raws] Shingeki no Kyojin (2020) 02 [BDRip 1920x1080 HEVC FLAC].mkv [9EFD583F]
└──Batch_Mux.py

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

## 7zip (Optional)

During the execution of the file, a prompt about the attachments would be asked, if the link is pasted then 7zip is used to extract the attachments folders and place them into the "append" folder.
If the "append" folder is already populated, this installation can be skipped.

7zip can be installed from the links mentioned below
> If installed, make sure 7zip has been added to PATH


> Make sure mkvmerge has been added to PATH or copy mkvmerge.exe to the root (or parent) folder for the script to detect mkvmerge

# Run

To run the script, open the terminal in the root folder and run
```
python Batch_Mux.py
```

# Links

[pymkv docs](https://pymkv.shel.dev/en/stable/)\
[mkvtoolnix](https://mkvtoolnix.download/downloads.html)\
[python](https://www.python.org/downloads/)\
[7zip](https://www.7-zip.org/)