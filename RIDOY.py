import os,platform,sys
os.system("git pull")
rmx=platform.architecture()[0]
if rmx=='64bit':
  import RR
if rmx=='32bit':
  import RR2
else:print('\033[1;32m[•] Contract Admin For Help');exit()
