#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import markdown
import glob
import os.path


header ='''
[Memo just for me](.)
===

'''

footer ='''
---

## Links

[Memo just for me](.)

[My official page](http://www.ok.sc.e.titech.ac.jp/~mtanaka/)

[My official github](http://github.com/mastnk/)

[My hobby page](http://like.silk.to/)

[My hobby github](http://github.com/likesilkto/)

'''

gfm = markdown.Markdown(output_format='html5', extensions=['gfm'])

files = glob.glob('*.md')
for file in files:
	basename = os.path.basename(file)
	titlename = os.path.splitext(basename) [0]
	
	with open(file, 'r') as fin:
		md = fin.read()
		
	md = header + md + footer
	html = gfm.convert(md)
	
	with open(titlename+'.html','w') as fout:
		fout.write(html)
	
	print( file + ' -> ' + titlename+'.html')
	
