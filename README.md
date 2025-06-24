To install the requirements, Run the below line inside of the Terminal of the local directory of the main machine learning project files:
```
pip install -r requirements.txt
```

To Run the Streamlit app:

First make sure the directory is properly opened in the terminal

then run
```
streamlit run app.py
```

*University Prediction Analyser for Admissions*

This Documentation is made to update the whole process and working done within the machine learning model. 
The main reason for making this model is to identify your chances of gainging the insights of chances for you to get into a University

**What is the dataset being used:**
    We will be using a Dataset which contains the necessary things for university admission for example Test scores, university rating, CGPA, letter of recommendation score, Statement of purpose, and research experience to find the chnaces of landing an admission into that university

**What does the Model do! (Code Level):**
    The model first imports the necessary libraries one by one for future uses
    Then the code will import the dataFrame of the already made prediction/ Actual values from real world scenarioes which has knowledgable insights of the data
    these datas are used to find / predict the probability of us getting into a University
    After this is done, We can visualize within the ipynb Code about the dataFrame.
##### Now we dive into Data PreProcessing:- 
        First of all we will clear out any Null Values If present
        Then we will remove all unwanted columns within the dataFrame
        If there is any Irregularities then we could perform ScalarStandardization or Normalization. But here we dont need to perform those since our data set is clear.
        If we wanted to, We could also perform One Hot encoding. But it is not suitable in this data
### Then we move on to the Visualization
        After visualizing the model, We can figure out some patterns and correlation between columns
        The HeatMap gave us insight on which column are dependent upon which other columns.
            Here, We found that the admission chances is mostly dependent upon the pre and final term tests and also the cgpa of a student
        Then from the LMPlot with facetgrid and regplots we figured out that people with lower scores of SOP and LOR tend to apply for low level universities. But some still apply for high tier universities in hopes of gaining the UG Admissions
        The final plot shows us the relationship between CGPA and The Universities rating when it comes to people who has a research experiencec and apply for these     
### Then we move on to the model Processing:- 
        After learning the insights about the data frames and how each columns are interconnected to each other, We can start processing the data so that we can predict the values
        First of all, We must split the dataframe into train and test data with 20% of the data going to testing process with random state of 65 and evaluating the model
        After consideration of the Machine learning models, We can go ahead and use Linear Regression to find out the probability
        We first declare the model and train the model using training dataset
### we predicted the values for evaluation and visualization
        After model training, we can predict the values for the test dataset so that we can fine tune the data model
        Model evaluation
            We will be using the MSE score which is commonly used for regression models like linear regression. 
            The lower the MSE score is, THe better our model is
            Then we will use the R2 score to find the goodness of fit. 
            The higher R2 score is required in order to find the better prediction
            Our model produced the following output before fine tuning:
                MSE Score:  0.0035511805450987085
                R^2 Score:  0.8263481396039751
            But After Fine tuning, Our model produced:
                MSE Score:  0.0028047791404953904
                R^2 Score:  0.8704504365542649
            The Evaluation metrics after fine tuning is better than the randomized metrics given at the start
        visualizing The Model:
            After creating the model, We finally start to visualize it by creating the differentiation of the values with Actual and the predicted values.
            This scatter plot shows us the meadian line and the scatter of datapoints which helps us to figure out how much error each points have from the meadian line
            The closer the point is to the line, The lesser the error occured
### Finally we store our data model in a pkl file for further demonstration/ applications
        we use pkl model storage to store our model using joblib and use the model outside of this file 

After occuring the model, we must use the model to visualize or create an interface for others to predict their chances of the oppurtunity of getting admission into a university
To resolve this issue, We can use Streamlit module which is made for Ui within python 

**Stream Lit Application**
    The Ui is made inside of the file named app.py, which contains the Streamlit code with some operations
    this Application will contain 3 main portals, Thier explanation as follows
    Portals of the Stream Lit App
        Portal 1 - Student Portal
            In this portal we can enter in our(student) data for prediction and it gives out a probability of chances we have to get into the university's admission process
            Here the main goal is to provide the students the chance they have to get into the university
        Portal 2 - College/ Universty Portal
            In this Portal, the Output is for the universities to know if the specified candidate is eligible for The college or not
            The portal outputs if they are better than expected or else if they dont need the requirements or so
        Portal 3 - Counsellor Portal
            The Counselling portal is used to identify which university is better for a student. 
            It would output the probability of getting placed in a university and also if they need to apply for better universities or not
            This way, we can know which level of university is better for applying and which university would give us better probability of getting into it and also offers if they likely to get into higher level universities
            Using this, counselling people can provide a better insight for the students for admission process
    
    Now lets dive into the code inside the application python file. ("app.py):
        First of all we will be importing in the necessary libraries which we use inside our code to run methods and functions
        We will import streamlit for the application UI, joblib for importing the trained model, and numpy for generating the dataset frame
        After importing the libraries, We will straight away import the model which have trained and stored inside of the model.pkl
        After importing the model. We will go ahead and create the application by giving the name/ title of the application  which will be shown at the top.
        Then, we will generate a selection box where people can choose which portal they want to use, For example if they want to use the student portal or the counseling portal or the university/college portal.
        Once we gain that info from the user, We will start by asking the user inputs which will be fed to our machine learning model and for predicting the insight.
        After gaining all the information we required. We can start arranging them in a 1D array using numpy
        Now we go into the process of prediction and outputting
            Once the user presses the predict button, The condition will satisfy and the control will go into the conditional statement 
            When the button is pressed, we will send the array of inputs to the model to predict the output of the data.
            After predicting the admission chance, We will convert the data from 0-1 range into 0-100 range by multiplying it so that we can visually look into it as a normal percentage.
            After all these, We will output for each desired Portals selected.
            If the selected portal is students, Then just the probability will be provided
            If the selected portal is university, Then the output will be provided with probability and also if the person is right for our univeristy or not 
            If the selected portal is Counselling, Then it will output the probability with the capability of the person if applying for a better college or not
        The application is made to interact with the machine learning model by the means of Better UI for interaction

This application needs to be ran in the terminal.
**To successfully running the streamlit app, Follow the below instructions**
    1 - Make sure you have your terminal opened to the correct directory. The directory must aim to the folder which contains the app.py file with the model.pkl file which was created by the Admission.ipynb
    2 - After navigating into the correct directory location, Type in the command ```streamlit run app.py```
    3 - This command would run a local host in the browser, Or you can also  access it by typing 'http://localhost:8501' in your web browser
    4 - After running the applcation we cna interact with the inputs using the sliders and also the drop boxes to find the prediction value of the student being admitted into the university by seleccting them for admission
     
###### This Project is made during Gradious's Hackathon conducted from june 23 till June 24 of 2025. 
###### All Rights for the code goes to Kanishk K S