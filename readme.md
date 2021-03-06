# Data_Tool
## Intro

This is a project that I've thought about for quite sometime now. In sometime, I mean years! Basically, I want to create a simple tool like Tableau or DOMO that will allow me to analyze 
simple CSV files. The basic functionality would be that you load a csv file and then can 
look the data through some basic data visualizations.

Part of this project has been built out and appears to work. You can upload any text document 
to it and it will tell you the sentiment analysis of that sentence. It also breaks the text 
document down and tells you other things like common word count, sentiment by sentence and 
graphs this for you. 

So this project, as of July of 21, has two main features:

1. Text document sentiment analysis.
2. CSV document data analysis - this will be a simple data dashboard.

The CSV document portion of this project is getting really bloated. It is something that I could 
in the future go back and fix. I've started to add comments to places in the code that I think 
need to be fixed. My first goal is to get it working at a basic level and then I may 
start looking at fixing things. 

I will say that I'm not sure if I'll ever finish this project. There may be parts that I can't 
figure out how to build. I may also continually be adding more and more parts to it as to 
build a fairly robust data tool. We'll see where this goes. For now it's time to start the adventure...

# Getting started
### Installing

Please note that these instructions are not 100% complete. 

1. Clone the repo
2. Run [sudo] pip3 install or pip3 install flask
3. Run python3 app.py to run the application
4. Visit localhost:5000 to see the application
5. Please note that these instructions only follow the Python side of this application.

### Technology Stack

1. Flask-0.12
2. Python-3.4
3. Pandas-0.18.1
4. Numpy-1.11.0
5. Vue.JS-2.5

Remix Icon link: 
https://remixicon.com/

### Operation

Once the program is downloaded, simply run the program as you would any other python program.
Then follow the address, which your console/terminal tells you to go to see the
website. Again, please do not forget to ensure that you have vue CLI installed
as well as npm.

# Issues / Other

1. The drag and drop for column names - need to fix having two names in one area briefly. 
2. The csv file page I think is getting quite overblown and could be changed in the future. 
	-Believe that the state management side of things could be heavily improved. 
3. Dealing with dates on the CSV file. 
4. I've thought about on the text analysis to present the entire document and highlighting 
a sentence as the use clicks through. The problem with this is that some documents may be 
to long so I decided not to go that route.

# Preview

To see a video that talks about this project please go here: COMING SOON