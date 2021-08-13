# miscellaneous

Program invocation must be as below:

$ echo "abc123" | python SumProgramMisc.py 

Output:  
6


$ echo "abc123" | python SumProgramMisc.py -x

Output:  
39


$ echo "qq" | python SumProgramMisc.py 

Output:  
0


$ echo "abc123" > file.tmp
$ python SumProgramMisc.py -f file.tmp

Output:  
6
