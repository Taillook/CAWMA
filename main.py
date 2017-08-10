# -*- encoding:utf8 -*-

import subprocess


cmd = "sudo arp-scan -l --interface en0 | grep -i '[0-9A-F]\{2\}\(:[0-9A-F]\{2\}\)\{5\}' | tr '\t' '|' | cut -d '|' -f2 | cut -d '|' -f1"
result = (str(subprocess.check_output(cmd, stderr=subprocess.STDOUT, shell=True, universal_newlines=True)).split("\n"))[0:-1]
print(result)
