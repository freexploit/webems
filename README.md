webems
======

A tool for rapidly editing a webpage, saving it, then serving out the modified copy.

Intended for people and organizations that have need to both (A) troubleshoot web pages they do not control, and then (B) quickly share those modifications with other parties. (Author's case, supporting third-party JavaScript applications that project managers, designers, and clients need to see.)

If only doing A, a real proxy tool (e.g. Charles Proxy) will give you better precision. 

Because of how some web pages are built, this tool doesn't work with every site. But it does work with quite a few. 

install
======

Application is built on python and django. You'd a server runing python 2.7.1, the python libraries listed in the project's requirements.txt, and an update to the database settings in settings.py. Currently set to sqlite, which has been working fine for ~150 or so emulations and about 80 users. 

Please don't ever make an installation of this available to the general public. Just think about it. 