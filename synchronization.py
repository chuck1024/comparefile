# -*- coding: utf-8 -*-

__author__='chuck1024'

import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import commands

#commands.getoutput("python /opt/comperfile/test.py")
while(1):
	a = raw_input(u'请确认(yes/no): ')
	if a == "yes":
		commands.getoutput("rm -rf /apps/bak/s01 /apps/bak/u01")
	
		commands.getoutput("cp -rf /apps/bak/s02/ /apps/bak/s01/")
		commands.getoutput("rm -rf /apps/bak/s02/")
	
		commands.getoutput("cp -rf /apps/bak/u02/ /apps/bak/u01/")
		commands.getoutput("rm -rf /apps/bak/u02/")
	
		commands.getoutput("cp -rf /apps/bak/u03/ /apps/bak/u02/")
		commands.getoutput("rm -rf /apps/bak/u03/")
	
		commands.getoutput("cp -rf /apps/s /apps/bak/s02/")
		commands.getoutput("rm -rf /apps/s")
		
		commands.getoutput("cp -rf /apps/u /apps/bak/u03/")
		commands.getoutput("rm -rf /apps/u")
	
		commands.getoutput("cp -rf /data/s /apps/")
		commands.getoutput("cp -rf /data/u /apps/")
	
		commands.getoutput("python /opt/comperfile/test.py")
		print u'成功！！！'
		break
	elif a == 'no':
		print u'请检查文件，做回滚操作！！！'
		break
	else:
		continue
