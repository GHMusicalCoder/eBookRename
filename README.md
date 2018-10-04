# eBookRename

This should be a simple program rename groups of eBook files for inclusion on devices, 
tracked through Calibre, and stored on a FreeNAS device.

The base goal of the program is to start a a given folder, loop through the subfolder,
and rename the files below based on the folder name.

As an example, from SitePoint, I downloaded their **8 Practical Bootstrap Projects** 
book.  When it downloaded (into a folder named "8 Practical Bootstrap Projects"), it
downloaded 3 files, one named bootstrap2.epub, another named bootstrap2.mobi, 
and one named boostrap2pdf.zip.

So what I want to happen is the following:
- Extract the pdf from the zip file
    - trickier because some of the zip files contain a __MAC-OS__ folder, and a 
    duplicate of all the files, not just the pdf file itself
- rename the extracted pdf file to the "folder name".pdf
- rename other files (epbu, mobi) to the "folder name".[proper suffix]
- delete the zip file
- rename the base folder, switching out spaces for underscores

so that when its all said and done, the structure looks like:

--- 8_Practical_Bootstrap_Projects

------ 8 Practical Bootstrap Projects.epub

------ 8 Practical Bootstrap Projects.mobi

------ 8 Practical Bootstrap Projects.pdf


Original Premise:

    eBookRename
        Get Startup Folder
        Step Through the Following
            Read Folder Name (Store)
            Format Directory - changing space to underscore
            Step into directory
            Unzip (if zip)
            Rename all files (.mobi, .epub, .pdf) using stored original folder name as file name