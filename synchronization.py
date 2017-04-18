# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding("utf-8")
import commands

#commands.getoutput("python /opt/comperfile/test.py")
while(1):
	a = raw_input(u'请确认(yes/no): ')
	if a == "yes":
		commands.getoutput("rm -rf /apps/bak/static01 /apps/bak/ui_template01")
	
		commands.getoutput("cp -rf /apps/bak/static02/ /apps/bak/static01/")
		commands.getoutput("rm -rf /apps/bak/static02/")
	
		commands.getoutput("cp -rf /apps/bak/ui_template02/ /apps/bak/ui_template01/")
		commands.getoutput("rm -rf /apps/bak/ui_template02/")
	
		commands.getoutput("cp -rf /apps/bak/ui_template03/ /apps/bak/ui_template02/")
		commands.getoutput("rm -rf /apps/bak/ui_template03/")
	
		commands.getoutput("cp -rf /apps/static /apps/bak/static02/")
		commands.getoutput("rm -rf /apps/static")
		
		commands.getoutput("cp -rf /apps/ui_template /apps/bak/ui_template03/")
		commands.getoutput("rm -rf /apps/ui_template")
	
		commands.getoutput("cp -rf /data/static /apps/")
		commands.getoutput("cp -rf /data/ui_template /apps/")
	
		commands.getoutput("python /opt/comperfile/test.py")
		print u'成功！！！'
		break
	elif a == 'no':
		print u'请检查文件，做回滚操作！！！'
		break
	else:
		continue
