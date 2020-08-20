# Sudoku 9*9 with Python
A useful website to ceate and solve sudukos : [qqwing](https://qqwing.com/)

If you want to know about the algorithms and heuristics you should search the web or read 

`Artificial Intelligence: A Modern Approach Textbook by Peter Norvig and Stuart J. Russell`

In each section (file) I updated the files to use less memory so in each step the number of nodes that we visit or create is decreasing and therefore the time that app spends to solve the sudoku is increasing (the speed is decreasing).

In other words the file `1.backtrack_and_FC.py` is the fastest but uses a lot of memory and the file `5.ac3Comp.py` is the slowest but uses small amount of memory.

In this part [here](#All-the-outputs-with-time-and-number-of-nodes-with-input3-file) I show you the time and nodes in files with `inpu3` file.

The `input3` file is the hardest sudoku ever :)

## Section 1 : Backtrack and forward checking `1.backtrack_and_FC.py`

In this section we only have backtrack and forward checking algorithms.

## Section 2 : Minimum Remaining Values `2.mrv.py`

In this section we update the section 1 file with Minimum Remaining Values (MRV).

## Section 3 : Least constrained value `3.lcv.py`

In this section we update the section 2 file with Least constrained value (LCV).

## Section 4 : Arc Consistency Algorithm #3 `4.ac3.py`

In this section we update the section 3 file with Arc Consistency Algorithm #3 (AC-3) I don't use queue in this section.

## Section 5 : Arc Consistency Algorithm #3 Complete `5.ac3Comp.py`

In this section we update the section 4 file with Arc Consistency Algorithm #3 (AC-3) I use queue to keep track of changed cells that need to be checked in AC-3 again.

## Sample inputs:

 The sample inputs are `input1` , `input2` and `input3` files, you can run the programms in UNIX with this command:

```bash
python 2.mrv.py < input1
```
The `input1` file is an easy sudoku.

After section 3 the app is slow so it's better to use pypy instead:

```bash
pypy3 4.ac3.py < input1
```

## Sample output:

> pypy3 3.lcv.py < input2

![Output](sample_output.png)

## All the outputs with time and number of nodes with input3 file

> time pypy3 1.backtrack_and_FC.py < input3
```bash
Number of nodes :  22068
pypy3 1.backtrack_and_FC.py < input3  2.00s user 0.03s system 98% cpu 2.063 total
```
---------------------------------------------------------------

> time pypy3 2.mrv.py < input3
```bash
Number of nodes :  9179
pypy3 2.mrv.py < input3  1.37s user 0.05s system 91% cpu 1.553 total
```
---------------------------------------------------------------

> time pypy3 3.lcv.py < input3
```bash
Number of nodes :  8354
pypy3 3.lcv.py < input3  1.32s user 0.05s system 98% cpu 1.389 total
```
---------------------------------------------------------------

> time pypy3 4.ac3.py < input3
```bash
Number of nodes :  9104
pypy3 4.ac3.py < input3  59.73s user 0.02s system 99% cpu 59.902 total
```
---------------------------------------------------------------

> time pypy3 5.ac3_comp.py < input3
```bash
Number of nodes :  6351
pypy3 5.ac3_comp.py < input3  160.58s user 0.07s system 99% cpu 2:41.10 total
```