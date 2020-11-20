# Grading-Homework
This is a script for easily grading the homework

The command to run the script is like this:
```
python3 exec_hw[1,5].py my_students.txt commands1.py commands2.py dir
```
or
```
python3 exec_hw[2,3].py my_students.txt commands1.py dir
```
where 

`my_students.txt` includes the names of the students, one in each line;

`commands.py` is the input that is needed when running the homework scripts, simply using print() would work as shown in the example code;

`dir` is the directory of all the downloaded homework scripts. Typically the default will be `submissions` unzipped from `submissions.zip`.
