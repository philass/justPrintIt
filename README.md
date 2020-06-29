# justPrintIt

justPrintIt automatically inserts and removes print statements. Super handy when a small program crashes and you need to find the line that the program crashes at (and for whatever reason its not obvious). justPrintIt is written in Python so it should just run.



## Running

If you want justPrintIt as a CLI tool you can simply add an alias
```bash
# in your .bash_profile .bashrc, .zshrc or equivalent
alias justprintit="/path/to/justPrintIt.py"
```

## Usage
Adding debug lines simply pass the -a flag.
Removing debug lines simply pass the -r flag.
```bash
$ justprintit

Usage : 
	justPrintIt -a fileName.cpp
	JustPrintIt -r fileName.cpp
```
