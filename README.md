# miscellaneous

Program invocation must be as below:

$ echo "abc123" | python SumProgramMisc.py 
6


$ echo "abc123" | python SumProgramMisc.py -x
39


$ echo "qq" | python SumProgramMisc.py 
0


$ echo "abc123" > file.tmp
$ python SumProgramMisc.py -f file.tmp
6
