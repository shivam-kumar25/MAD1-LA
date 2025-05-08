

"""
📁 Project Description:
-----------------------
This project is a Flask-based web application designed to read student marks from a 
CSV file (`data.csv`) and display relevant information based on user input via an 
HTML form. The application handles two query types:
    1. Student ID: Displays all course marks of a student and total marks.
    2. Course ID: Displays average and maximum marks of a course and a histogram.
"""






########################################################################################################
########################################################################################################
########################################################################################################
""" Import Flask and its modules for web app functionality """
########################################################################################################
########################################################################################################
########################################################################################################
from flask import Flask # Import Flask to create a web application

from flask import render_template # Import render_template to render HTML templates

from flask import request  # Import request to handle incoming requests







########################################################################################################
########################################################################################################
########################################################################################################
""" Import necessary libraries for data handling and visualization """
########################################################################################################
########################################################################################################
########################################################################################################
from matplotlib import pyplot as _plt  # Import pyplot from matplotlib for plotting graphs

import csv  # Import csv module to handle CSV file operations









##########################################################################################################################
##########################################################################################################################
""" Initialize the Flask application """
##########################################################################################################################
##########################################################################################################################
app_ = Flask(__name__)  











##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
""" Define the route for the default path """
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
@app_.route('/', methods=['GET', 'POST']) 
def task_():
    

    ################################
    # 
    ################################
    if request.method == 'GET':  
        # the server will return a html form to fill details
        return render_template('index.html') 
    
    

    
    ################################
    # 
    ################################
    with open(r"data.csv", newline='') as given_csv_file:  # Open the CSV file in read mode
        data_readed_ = csv.reader(given_csv_file)  # Read the CSV file using csv.reader
        
        
        
        ################################
        #  
        ################################
        if request.method == 'POST':  # Check if the request method is POST to handle form submission
            studnet_course_ = []  # Initialize an empty list to store student course data
            course_marks_ = []  # Initialize an empty list to store course marks
            
            
            ################################
            # 
            ################################
            select_id_ = request.form.get('ID')  
            value_id_ = request.form.get('id_value')  





            
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            """ Student ID: Displays all course marks of a student and total marks. """
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            if select_id_ == "student_id":  
                total_ = 0  # Initialize a variable to store the total marks for the student
                
                
                ################################
                # 
                ################################
                for row_ in data_readed_:  
                    if value_id_ in row_[0]: 
                        total_ += int(row_[2].strip()) 
                        studnet_course_.append(row_) 
                    
                    
                    
                ################################
                # The application should display an error message if there is a deviation from the expected input.
                ################################
                if studnet_course_ == []:  # Check if no matching student data was found
                    return render_template('wrong.html')  # Render an error page if no data is found
            
                else:
                    # Render the student data page with the retrieved data and total marks
                    return render_template('student_data_.html', student_course=studnet_course_, total_marks_data=total_)






            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            """ Course ID: Displays average and maximum marks of a course and a histogram. """
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            ###########################################################################################
            if select_id_ == "course_id":  # Check if the selected ID type is "course_id"
                for row_ in data_readed_:  # Iterate through each row in the CSV file
                    
                    ################################
                    # 
                    ################################
                    if value_id_ in row_[1]:  # Check if the input value matches the course ID in the row
                        course_marks_.append(int(row_[2].strip()))  # Append the marks to the course marks list
                    



                ################################
                # The application should display an error message if there is a deviation from the expected input.
                ################################
                if course_marks_ == []:  # Check if no matching course data was found
                    return render_template('wrong.html')  # Render an error page if no data is found
            
                else:
                    average_marks_ = sum(course_marks_) / len(course_marks_)  # Calculate the average marks
                    max_marks_ = max(course_marks_)  # Find the maximum marks
                    
                    
                    
                    
                    _plt.clf()  # Clear the current figure to avoid overlapping plots
                    ################################
                    # making the histogram
                    ################################
                    _plt.hist(course_marks_, bins=10)  
                    _plt.ylabel("Frequency")  
                    _plt.xlabel("Marks")  
                    _plt.xlim(20, 100)  
                    _plt.savefig(r"\static/marks_hist.png") 
                    
                    
                    
                    ################################
                    # Render the course data page with the calculated average and maximum marks
                    ################################
                    return render_template("course_data_.html", average_marks=average_marks_, maximum_marks=max_marks_)








##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
""""  """
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
##########################################################################################################################
if __name__ == "__manin__": 
    app_.run(debug=True)  