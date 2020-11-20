#!/usr/bin/python3
## Grading script 
## Author: Yunming Xiao

from subprocess import Popen, PIPE
import os, glob
import sys
import time

def get_students(filename):
    student_fullname = {}
    fp = open(filename, 'r')
    for line in fp:
        sn = line.strip().lower().replace("-", "").replace("\'", "").split(' ')
        abbr = ''.join([sn[-1]] + sn[:-1])
        student_fullname[abbr] = line.strip()
    return student_fullname

def get_hw_submission(prefix, student_fullname):
    student_list = {}
    fps = os.listdir(prefix)
    for fp in fps:
        student_name = fp.split('_')[0]
        if student_name in student_fullname:
            student_list[student_name] = fp
    return student_list

def run_hw(student_fullname, student_list, command_file1, command_file2, prefix):
    for student in student_fullname:
        print('# ---------------------------------- #')
        if student not in student_list:
            print('File not found for %s' % (student_fullname[student]))
        else:
            try:
                print('Executing the Python script of %s' % (student_fullname[student]))
                if '.zip' in student_list[student]:
                    p1 = Popen(["unzip", "%s/%s" % (prefix, student_list[student]), '-d', "%s/%s" % (prefix, student_list[student][:-4])], stdout=PIPE)
                    p1.wait()
                    print('%s/%s/**/*.py' % (prefix, student_list[student][:-4]), glob.glob('%s/%s/**/*.py' % (prefix, student_list[student][:-4])))
                    for fp in glob.glob('%s/%s/**/*.py' % (prefix, student_list[student][:-4]), recursive = True):
                        print(fp)
                        print("------------------ First ------------------")
                        p1 = Popen(["python3", command_file1], stdout=PIPE)
                        p2 = Popen(["python3", fp], stdin=p1.stdout, stdout=PIPE)
                        p1.stdout.close()
                        output = p2.communicate()[0].decode('utf-8')
                        print('Results:')
                        print(output)
                        
                        print("------------------ Again ------------------")
                        p1 = Popen(["python3", command_file1], stdout=PIPE)
                        p2 = Popen(["python3", fp], stdin=p1.stdout, stdout=PIPE)
                        p1.stdout.close()
                        output = p2.communicate()[0].decode('utf-8')
                        print('Results:')
                        print(output)

                        print("------------------ Second ------------------")
                        p1 = Popen(["python3", command_file2], stdout=PIPE)
                        p2 = Popen(["python3", fp], stdin=p1.stdout, stdout=PIPE)
                        p1.stdout.close()
                        output = p2.communicate()[0].decode('utf-8')
                        print('Results:')
                        print(output)

                        print("------------------ Again ------------------")
                        p1 = Popen(["python3", command_file2], stdout=PIPE)
                        p2 = Popen(["python3", fp], stdin=p1.stdout, stdout=PIPE)
                        p1.stdout.close()
                        output = p2.communicate()[0].decode('utf-8')
                        print('Results:')
                        print(output)
                else:
                    print("------------------ First ------------------")
                    p1 = Popen(["python3", command_file1], stdout=PIPE)
                    p2 = Popen(["python3", "%s/%s" % (prefix, student_list[student])], stdin=p1.stdout, stdout=PIPE)
                    p1.stdout.close()
                    output = p2.communicate()[0].decode('utf-8')
                    print('Results:')
                    print(output)

                    print("------------------ Again ------------------")
                    p1 = Popen(["python3", command_file1], stdout=PIPE)
                    p2 = Popen(["python3", "%s/%s" % (prefix, student_list[student])], stdin=p1.stdout, stdout=PIPE)
                    p1.stdout.close()
                    output = p2.communicate()[0].decode('utf-8')
                    print('Results:')
                    print(output)

                    print("------------------ Second ------------------")
                    p1 = Popen(["python3", command_file2], stdout=PIPE)
                    p2 = Popen(["python3", "%s/%s" % (prefix, student_list[student])], stdin=p1.stdout, stdout=PIPE)
                    p1.stdout.close()
                    output = p2.communicate()[0].decode('utf-8')
                    print('Results:')
                    print(output)

                    print("------------------ Again ------------------")
                    p1 = Popen(["python3", command_file2], stdout=PIPE)
                    p2 = Popen(["python3", "%s/%s" % (prefix, student_list[student])], stdin=p1.stdout, stdout=PIPE)
                    p1.stdout.close()
                    output = p2.communicate()[0].decode('utf-8')
                    print('Results:')
                    print(output)
            except Exception as e:
                print("Exception! %s \n%s" % (student_fullname[student], e))
        print('# ---------------------------------- #\n\n\n')
        input("Press enter key to continue...")

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print('Usage: python3 exec_hw.py my_students.txt commands1.py commands2.py directory')
        exit()
    student_fullname = get_students(sys.argv[1])
    student_list = get_hw_submission(sys.argv[4], student_fullname)
    run_hw(student_fullname, student_list, sys.argv[2], sys.argv[3], sys.argv[4])
