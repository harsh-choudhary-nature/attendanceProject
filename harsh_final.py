import os
import harsh_math as hm
def get_csv_file_names():
    files=os.listdir()
    csv_list=[]
    stu_dict={}
    for file_name in files:
        if file_name[-4:]==".csv":
            csv_list.append(file_name)
    for file in csv_list:
        fh=open(file,'r')
        for line in fh:
            line=line.strip()
            stulist=line.split(',')
            if stulist[1].isnumeric():
                if stulist[0] not in stu_dict.keys():
                    stu_dict[stulist[0]]=[stulist[1]]
                else:
                    stu_dict[stulist[0]]=stu_dict[stulist[0]]+[stulist[1]]
    return stu_dict
def writer(dict1,file1):
    file_writer=open(file1,'w')
    list1=list(dict1.keys())
    list1.sort()
    for student in list1:
        file_writer.write(student)
        file_writer.write('\n')
def writer_attendance(dict1,file1):
    file_writer=open(file1,'w')
    for key in dict1:
        file_writer.write(key+" ")
        file_writer.write(str(len(dict1[key])))
        file_writer.write(" ")
        file_writer.write(str(dict1[key]))
        file_writer.write("\n")

student_attendance_dictionary=get_csv_file_names()
writer(student_attendance_dictionary,'students.txt')
writer_attendance(student_attendance_dictionary,'students-attendance.txt')

#for computing histogram
list_all=[]
for key in student_attendance_dictionary:
    list_all+=student_attendance_dictionary[key]
for i in range(0,len(list_all)):
    list_all[i]=int(list_all[i])
hist_dict=hm.comp_histogram(list_all)
print(hist_dict)
