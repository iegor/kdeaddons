#!/usr/bin/python

### Copyright (C) 2001 Jesper K. Pedersen
### This program is free software; you can redistribute it and/or modify
### it under the terms of the GNU General Public License as published by
### the Free Software Foundation; either version 2 of the License, or
### (at your option) any later version.
###
### This program is distributed in the hope that it will be useful,
### but WITHOUT ANY WARRANTY; without even the implied warranty of
### MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
### GNU General Public License for more details.
###
### You should have received a copy of the GNU General Public License
### along with this program; if not, write to the Free Software
### Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA 02110-1301, USA.

import urllib, re,string

################################################################################
# Groups of interest
################################################################################
interest=['Forsiden', 'Sidste nyt', 'Indland', 'Udland', 'Odense', 'Fyn', 'Erhverv', 'Computer']

base="http://www.fyens.dk/blinde/"
articleBase = "http://www.fyens.dk/"

################################################################################
# Query the sections
################################################################################
def readSections():
  FILE=urllib.urlopen(base+"Menu.php")
  REG=re.compile("<a href=\"([^\"]*)\" target=\"Indhold\" class=\"Overskrift.\">(.*?)</a><br>")
  result=[]
  line=FILE.readline()
  while line:
    match = REG.search(line)
    if match:
      result.append( match.groups() )
      
    line=FILE.readline()
  FILE.close()
  return result

################################################################################
# Fetch articles from a single section
################################################################################
def readSection( url, title ):
  FILE=urllib.urlopen(base+url)
  REG=re.compile("<a href=\"([^\"]*)\" class=\"Overskrift.\">(.*?)</a>")
  line = FILE.readline()
  while line:
    match = REG.search(line)
    if match:
      print "<item>\n\t<title>" + title + ": " +match.group(2) + "</title>"
      print "\t<link>"+articleBase+match.group(1)+"</link>\n</item>"
    line=FILE.readline()

################################################################################
# Print Header
################################################################################
print """<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE rss PUBLIC "-//Netscape Communications//DTD RSS 0.91//EN"
 "http://my.netscape.com/publish/formats/rss-0.91.dtd"> 
<rss version="0.91">
<channel>
<title>Fyens Stiftstidende</title>
<language>dk</language>
<link>http://www.fyens.dk/</link>
<description>Fyens Stiftstidende</description>
"""

################################################################################
# Main
################################################################################
l = readSections()
for (url, title) in l:
  if ( interest.count( title ) ):
    readSection(url, title)

################################################################################
# Print footer.
################################################################################
print """
</channel>
</rss>
"""

 