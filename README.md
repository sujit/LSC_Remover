Local Security Check (LSC) NVTs Remover
========================================
Description:
Script to remove LSC checks from OpenVAS NVT Plugins directory.

Module requirements:
* fnmatch [Should be there by default]
* User access permission (both read/write) to the OpenVAS plugins directory and the contents inside them.

Script usage:
* $ sudo chmod a+x lsc_remover.py
* $ sudo python lsc_remover.py

Script will perform the following actions:
* Navigate to /var/lib/openvas/plugins directory and scan for the presence of all OpenVAS LSC based NVTs.
* Make the list of all the NASL and ASC files those needs to be deleted.
* Delete the filtered files one-by-one.
* After removal of all the files, please run openvasmd --rebuild to generate the new NVTs cache.
  That's it!

Feedbacks:
Please drop an email to: thesujit [at] gmail [dot] com if you have any suggestions/feedbacks.
