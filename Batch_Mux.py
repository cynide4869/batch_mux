# Muxes subs, attachments and chapters into a mkvfile
from pathlib import Path
import pymkv

parent_directory = (Path.cwd()).resolve()
mkvfiles_directory = (parent_directory / 'mkvfiles').resolve()
attachments_directory = (parent_directory / 'attachments').resolve()
output_directory = (parent_directory / 'output').resolve()

def create_folder():
	'''Creates the output folder if it doesn't already exist'''

	if not output_directory.exists():
		output_directory.mkdir()


def get_list(source_directory):
	'''Returns a list of items present in a directory specified by the parameter'''

	temp_list = [item for item in source_directory.iterdir()]
	return sorted(temp_list)


def append(attachments_folder, mkv):
	'''Appends the fonts, subtitle tracks and chapters if present'''

	font_folders = []
	subs = []
	chapter = None

	for item in attachments_folder.iterdir():
		if item.is_dir():
			font_folders.append(item)
		elif item.suffix == '.ass':
			subs.append(item)
		elif 'chapters' in item.name.lower() and item.suffix == '.xml':
			chapter = item
		else:
			continue

	if font_folders:
		print('\nAdding fonts:\n')
		for font_folder in font_folders:
			for font in font_folder.iterdir():
				print('{}'.format(font.name))
				mkv.add_attachment(str(font))
	else:
		print('\nNo fonts present')

	if subs:
		print('\nAdding subtitles:\n')
		for subtitle in subs:
			print('{}'.format(subtitle.name))
			mkv.add_track(str(subtitle))
	else:
		print('\nNo subtitles present')

	if chapter:
		print('\nAdding chapter: ', chapter.name)
		mkv.chapters(str(chapter))
	else:
		print('\nNo chapters present')


def muxing(mkv, mkvfile):
	'''Muxes the mkv file with the changes made'''

	mkv.mux(output_directory / mkvfile.name, silent=True)
	print('Done\n----------------------------------')


def main():
	create_folder()
	mkvfiles = get_list(mkvfiles_directory)
	attachments = get_list(attachments_directory)

	for i, mkvfile in enumerate(mkvfiles):
		print('Working File: ', mkvfile.name)
		mkv = pymkv.MKVFile(mkvfile)
		append(attachments[i], mkv)
		muxing(mkv, mkvfile)


if __name__ == '__main__':
	main()