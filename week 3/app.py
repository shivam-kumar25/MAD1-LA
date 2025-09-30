


#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
''' The python program must generate an output HTML document named "output.html:" and an image ( as required by the problem statemnt)
in the current working directory.'''
#################################################################################################################################
################################################################################################################################
##############################################################################################################################



#################################################################################################################################
##################################################################################################################################
##################################################################################################################################
""" The python program must take as input two parameters as command-line arguments.
example input : python app.py -c 2001
example input : python app.py -s 1007 """
###################################################################################################################################
##################################################################################################################################
##################################################################################################################################



################################################################################################################################
#################################################################################################################################
#################################################################################################################################
""" The first parameter is either "-s" or "-c".
"-s" specifies that the second parameter is a student ID 
"-c" specifies that the second parameter is a course ID """
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################



#################################################################################################################################
#################################################################################################################################
#################################################################################################################################
""" If the first parameter is "-s",
Then the second parameter should be a student id.
From the input CSV, the program must extract marks for each course, of the student whose ID is given as the second parameter."""
################################################################################################################################
""" The code must create an HTML page that displays the output in a tabular form (the order of colums must remains the same)."""
################################################################################################################################
""" The table should be title as "Student Details" and should have columns headers: "Student ID" and "Course ID" and "Marks". The table should also display
the totla marks of that student in the last row. """
#################################################################################################################################
#################################################################################################################################
#################################################################################################################################



##################################################################################################################################
##################################################################################################################################
##################################################################################################################################
""" If the first parameter is "-c",
Then the second parameter should be course ID.
The python program must find the highest and the average marks and the average marks for that course and display it on an HTML page"""
####################################################################################################################################
""" The title of the table must be "Course Details" and the coulms header must be "Average Marks" and "Maximum Marks" (the order must remain the same)"""
###################################################################################################################################
""" The pyton code must also display the histogram of marks for the given course ID."""
##################################################################################################################################
##################################################################################################################################
##################################################################################################################################



###################################################################################################################################
###################################################################################################################################
###################################################################################################################################
""" The program should dispalay an error message if there is a deviation from the expected input."""
###################################################################################################################################
""" For instance if "-s" is followed by course ID or any invalid studnet ID, theb a message must be displayed on the HTML page. """
####################################################################################################################################
####################################################################################################################################
###################################################################################################################################



# html doesen't have a thing called varialble 
# create one html page with variables having crtly brackets
# convert it into jinja template
# render it by giving the value that we want it to



############################################################################################################################### 
########### sys module helps to interact with command-line arguments     ###################################################### ##############################################################################################################################
import sys 

################################################################################################################################
######  This is used to plot graphs,  ############################################################################################
# ################################################################################################################################
import matplotlib.pyplot as plt_ 

############################################################################################################################## 
########### This module allows reading and writing CSV files ###################################################################
#################################################################################################################################
import csv 

################################################################################################################################## 
####### This module will help us in making HTML document   ##########################################################################
###################################################################################################################################
from jinja2 import Template  





################### This expression is used to read the command-line argument ###############################################
input_command_list_ = sys.argv





####################### open the csv file in the same folder #######################################################################
################################ Open the file and create a reader object ########################################################### 
############################# Reading the CSV file ################################################################################
with open(r"data.csv",'r', newline='' ) as csv_file_given_ :
    csv_file_data_ = csv.reader(csv_file_given_)
    
    
    
    
    #################### CSV file format:  [Student id, Course id, Marks]
    
    


     
    #############################################################################################################################
    ######## part 1) -s then calculate then render
    ######## part 2) -c then calculate then render 
    ######### part 3) somthing wrong 



    """
    ################################################################################################################################
    ################################################################################################################################
    ################################################################################################################################
    #############   part-1   
    ############# input_command_list ==  [ "script_name" , "-s" , "Studnet ID"]
    #############   example input : python app.py -s 1007
    ################################################################################################################################
    ############     output : extract Course ID and marks for each course whose Student ID is given as second parameter
    ############     also calculate the total marks
    ################################################################################################################################
    ################################################################################################################################
    ################################################################################################################################
    """
    student_course_s_ = []   #  list of the rows [Student id, Course id, Marks] that correspond to the inputed Student ID 
    total_marks_ = 0       # initilize to zero for calculatin the total marks of all courses.



    if input_command_list_[1] == '-s':
        for row_ in csv_file_data_:
            if input_command_list_[2] in row_[0]:
                total_marks_ += int(row_[2].strip())
                student_course_s_.append(row_)

    

        if student_course_s_ == []:  #  this means the id is wrong or not avilabel in the given CSV file. 
            output_error_message_ = """ 
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Document</title>
                </head>
                <body>
                    <h1> Wrong Inputs </h1> 
                    <p> Something went wrong </p>
                </body>
            </html>"""
        # we render only when there is a variable, but this is a static html having no variable elements, so no jinja2 required
            output_file_ = open('output.html' , 'w')
            output_file_.write(output_error_message_)
            output_file_.close()


        #########################################################################################################################
        #########  {{}}   used for variable,
        ########   {}     condition statement
        ########################################################################################################################
        else:
            html_output_ = """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8" />
                <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Document</title>
                </head>
                <body>
                    <h1> Student Details </h1>  
                    <table border="2px"> 
                        <tr>
                            <th> Student id </th>
                            <th> Course id </th>
                            <th> Marks </th>
                        </tr>
                        {% for student in student_course %}
                            <tr>
                                <td> {{ student[0].strip() }} </td>
                                <td> {{ student[1].strip() }} </td>
                                <td> {{ student[2].strip() }} </td>
                            </tr>
                        {% endfor %}
                        <tr> 
                            <td colspan="2"> Total Marks </td>
                            <td> {{ total }} </td>
                        </tr>
                    </table>
                </body>
            </html>
            """
            temp_ = Template(html_output_)
            output_1_ = temp_.render( total = total_marks_ , student_course=student_course_s_ )
            file__ = open('output.html' , 'w' )
            file__.write(output_1_)
            file__.close()
            
    
    
    
    
    """
    ############################################################################################################################# 
    ############################################################################################################################
    ############################################################################################################################
    ###############   part-2
    ###############   example input : python app.py -c 2001
    ###############   input_command_list ==  [ "script_name" , "-c" , "Course ID"]
    #############################################################################################################################
    ###############   output : find the highest marks and average marks corresponds to that Course ID inputed as second parameter 
    ###############   in command-line argument. 
    ###############   A histogram of marks for the given Course id.
    ############################################################################################################################
    ############################################################################################################################
    ##############################################################################################################################
    """
    student_course_c_ = []   #  list of the rows [Student id, Course id, Marks] that correspond to the inputed Course ID
    maximum_marks_ = 0       # highest marks corresponds to the given course ID
    average_marks_ = 0       # average makrs corresponds to the given course ID
    
    
    
    if input_command_list_[1] == '-c':
        for row_ in csv_file_data_:
            if input_command_list_[2] in row_[1]:
                student_course_c_.append(row_)
        
        
        if student_course_c_ == []:  #  this means the id is wrong or not avilabel in the given CSV file. 
            output_error_message_ = """ <!DOCTYPE html>
            <html lang="en">
                <head>
                <meta charset="UTF-8" />
                <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                <title>Document</title>
                </head>
                <body>
                    <h1> Wrong Inputs </h1> 
                    <p> Something went wrong </p>
                </body>
            </html> """
            
            # we render only when there is a variable, but this is a static html having no variable elements, so no jinja2 required
            output_file_ = open('output.html' , 'w')
            output_file_.write(output_error_message_)
            output_file_.close()
        
        
        else:
            
            ######  calculating the average and maximum 
            marks_list = []
            for marks_ in student_course_c_:
                marks_list.append(int(marks_[2]))
            maximum_marks_ = max(marks_list)
            average_marks_ = sum(marks_list)/len(marks_list)
            
            #########################################################################################################################
            ####### creating the histogram,
            #########################################################################################################################
            marks_data = marks_list
            plt_.hist(marks_data)
            plt_.xlabel("Marks")
            plt_.ylabel('Frequency')
            plt_.savefig("marks_hist.png")
            
            #########################################################################################################################
            #########  {{}}   used for variable,
            ########   {}     condition statement
            ########################################################################################################################
            html_output_ = """
            <!DOCTYPE html>
            <html lang="en">
                <head>
                    <meta charset="UTF-8" />
                    <meta http-equiv="X-UA-Compatible" content="IE=edge" />
                    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
                    <title>IIT Madras</title>
                </head>
                <body>    
                    <h1> Course Details </h1>  
                    <table border="2px"> 
                        <tr>
                            <th> Average Marks </th>
                            <th> Maximum Marks </th>
                        </tr>
                        <tr>
                            <td> {{ _average_ }} </td>
                            <td> {{ _max_ }} </td>
                        </tr>
                    </table>
                    <img src="marks_hist.png">
                </body>
            </html>
            """
            temp_ = Template(html_output_)
            output_1_ = temp_.render( _average_ = average_marks_ , _max_ = maximum_marks_ )
            file__ = open('output.html' , 'w' )
            file__.write(output_1_)
            file__.close()
                            
    
######################################################################################################################################
######################################################################################################################################
#################    input Example : python app.py -c 2001
#################    input Example : python app.py -s 1007
######################################################################################################################################
######################################################################################################################################