# Muxes subs, attachments and chapters into a mkvfile
from pathlib import Path
import pymkv

parent_directory = (Path.cwd()).resolve()
mkvfiles_directory = (parent_directory / 'mkvfiles').resolve()
attachments_directory = (parent_directory / 'append').resolve()
output_directory = (parent_directory / 'output').resolve()

def create_folder():
	'''Creates the output folder if it doesn't already exist'''

	if not output_directory.exists():
		output_directory.mkdir()


def get_list(source_directory):
	'''Returns a list of items present in a directory specified by the parameter'''

	temp_list = [item for item in source_directory.iterdir()]
	return sorted(temp_list)


def append(attachments_folder, mkv, insert):
	'''Appends the fonts, subtitle tracks and chapters if present'''

	font_folders = []
	subs = []
	chapter = None

	for item in attachments_folder.iterdir():
		if item.is_dir() and '2' not in insert:
			font_folders.append(item)
		elif item.suffix == '.ass' and '3' not in insert:
			subs.append(item)
		elif ('chapters' in item.name.lower() and item.suffix == '.xml') and '1' not in insert:
			chapter = item
		else:
			continue

	if font_folders:
		print('\nAdding fonts:')
		for font_folder in font_folders:
			for font in font_folder.iterdir():
				print('--{}'.format(font.name))
				mkv.add_attachment(str(font))
	else:
		print('\nNo fonts to append')

	if subs:
		print('\nAdding subtitles:')
		for subtitle in subs:
			print('--{}'.format(subtitle.name))
			mkv.add_track(str(subtitle))
	else:
		print('\nNo subtitles to append')

	if chapter:
		print('\nAdding chapter:\n--{}'.format(chapter.name))
		mkv.chapters(str(chapter))
	else:
		print('\nNo chapters to append')


def muxing(mkv, mkvfile):
	'''Muxes the mkv file with the changes made'''

	mkv.mux(output_directory / mkvfile.name, silent=True)
	print('\nDone.')


def ignore_existing(mkv, choice):
	'''Ignore certain MKV file properties which are present in the file'''

	if '0' in choice:
		return

	print('\nIgnoring the following properties present in the file')
	if '1' in choice:
		print('--chapters')
		mkv.no_chapters()
	if '2' in choice:
		print('--attachments')
		mkv.no_attachments()
	if '3' in choice:
		print('--global tags')
		mkv.no_global_tags()
	if '4' in choice:
		print('--track tags')		
		mkv.no_track_tags()


def main():
	create_folder()
	mkvfiles = get_list(mkvfiles_directory)
	attachments = get_list(attachments_directory)

	print('\nChoose the properties to ignore which are already present in the file (Remove properties in the final output)')
	print('--1) Chapters\n--2) Attachments (Fonts)\n--3) Global Tags\n--4) Track Tags')
	existing = input('Enter the numbers (Enter 0 to skip this menu): ')

	print('\nChoose the properties to ignore which are to be appended to the file (Won\'t append to the final output)')
	print('--1) Chapters\n--2) Attachments (Fonts)\n--3) Subtitles')
	insert = input('Enter the numbers (Enter 0 to skip this menu, adds all the files present in the attachments folder): ')

	for i, mkvfile in enumerate(mkvfiles):
		print('---------------------------------------------------------------------------')
		print('\nWorking File: ', mkvfile.name)
		mkv = pymkv.MKVFile(mkvfile)
		ignore_existing(mkv, existing)
		append(attachments[i], mkv, insert)
		muxing(mkv, mkvfile)


if __name__ == '__main__':
	main()