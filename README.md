# miscellaneous

Program invocation must be as below:

$ echo "abc123" | python SumProgramMisc.py 

O/P:  
6


$ echo "abc123" | python SumProgramMisc.py -x

O/P:  
39


$ echo "qq" | python SumProgramMisc.py 

O/P:  
0


$ echo "abc123" > file.tmp
$ python SumProgramMisc.py -f file.tmp

O/P:  
6
