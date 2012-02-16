#!/usr/bin/env python

# NOTES
# div's all default to hidden

import re

OUTPUT_FILE = "bcp.html";
INPUT_FILE = "bcp11.txt";

RE_PAGE = "^<[Pp]age (?P<pageNumber>\d+)>"

def findPageNumber(f, line):
  match = re.search(RE_PAGE, line)
  # match returns None (falsy) or MatchObject (truthy)
  if match:
    f.write('</pre>')
    f.write('<p class="bcp_page_number">{0}</p>\n'.format(int(match.group('pageNumber')) - 1))
    f.write('</div>\n\n')
    f.write('<div class="bcp_page" id="page{0}" style="display:none;">\n'.format(match.group('pageNumber')))
    f.write('<pre>')
  return match

def addNavigationBar(f):
  f.write('<input type="submit" name="navigateLeft" value="Navigate Left" id="navigateLeft" />')
  f.write('<div id="navigationInfo"></div>')
  f.write('<input type="submit" name="navigateRight" value="Navigate Right" id="navigateRight" />')

def scrub(line):
  return line.translate(None, "<>")

def main():
  with open(OUTPUT_FILE, 'w') as f:
    addNavigationBar(f)
    with open(INPUT_FILE, 'r') as bcp:
      f.write('<div class="bcp_page" id="page0" style="display:none;">')
      f.write('<pre>')
      for line in bcp:
        if findPageNumber(f, line):
          continue
        line = scrub(line)
        f.write(line)
    f.write('</pre>')
    f.write('</div>\n') # close last page


if __name__ == "__main__":
    main()
