# Digital BCP

A sandbox for experiments/learning.

## Quick start
Clone the git repo
Run bin/build.py to regenerate index.html
Run bin/scan.py to check certain features of the source file, bcp11.txt
Modify build.py and bcp11.txt to improve the accuracy of the text / formatting

## Contributing
Contributions welcome. Fork, modify, issue a pull request.

## To Do
### General
* Deploy with digitalbcp.org
* Clean up bcp11.txt 
	- investigate getting a fresh RTF (corrected) and parsing it out
	- fix missing/misplaced/duplicate page numbers
	- convert to markdown?
	- Remove/modify header per instructions
* Icon
* Bug report email

### build.py
* page face attribute
* assemble/minify/gzip plugins.js, scripts.js


### javascript / html / css
* A stylesheet to recreate the appearance of the real BCP as nearly as possible
* Floating navigation bar
	- images instead of hacky form buttons
	- Links (in drop-down?) (TOC in navigation bar, page selector)
* Bookmarks
	- colored vertical stripes (ribbons) in nav-bar
	- set via GUI or via url parameter
	- save in local storage
* About with license (CC) and credits (page 0, only accessible via direct link)
* Navigation by swiping
* Provide links for bookmarking parameters
* Better MVC separation?

## Features
* Go directly to page with ?page=n parameter in url
* If no parameter offered, return to last page viewed, else title page

## License
Base text: 
	"This file, which should be called BCP10.TXT or bcp10.txt, is in the 
	PUBLIC DOMAIN.  You may make copies, distribute them, produce derivative 
	works, reformat, and make extracts from it.  If you do so, please do not 
	distribute this header along with your altered E-text."

Header also states: "the text itself is guaranteed to be in the Public Domain by Canon Law"

I need to go find an appropriate license. Probably one of the looser Creative Commons licenses. I intend that my work (and any that should happen to be contributed to me) should be free to use and modify.

## Sources:
* [HTML5 Boilerplate](http://html5boilerplate.com)
* http://justus.anglican.org/resources/bcp/ASCII_1979.htm
* simple url parser: http://www.netlobo.com/url_query_string_javascript.html
* http://westcoastlogic.com/lawnchair/
