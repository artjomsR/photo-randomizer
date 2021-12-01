# photo-randomizer

A script I wrote after discovering that my digital photo frame has a limit to how many photos it can display. It creates a copy of a photo library and randomly deletes a percentage of all photos in all subfolders - the resulting directory should be a near perfect fit for copying to the photo frame storage device.

Needs Python 3. To run, edit the file `.py` file first to set the variables at the top. If the files in the photo library are not separated into subfolders, then `folder_separator` string will be used to put files into their respective folders.