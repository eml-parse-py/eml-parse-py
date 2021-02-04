# eml-parse-py

## Purpose:
A web app that analyses, with the email headers attached. Scroll down to CLI App if you want to use the CLI args.

### To run:
##### BACKEND: 
```
 
Create an environment variable 

set / export  FLASK_APP=app.py <- This lets the below command "flask run" work.
set / export FLASK_ENV=development <- This sets the app to debug mode 
set / export 
flask run

For reference:

export for *NIX/ MacOS systems
set for Windows systems
```

##### FRONTEND i.e. ReactKS
 ```
Start the application:
npm start 
```


## Technology stack in use:

- Python 3.7 minimum
- Flask API (this is backend of the system)
- ReactJS for the Frontend rendering...
- ReactBootstrap for styling

### Requirements:

- Python at least 3.8
- ReactJS 
- Flask API


## Installation:

- python -m pip install requirements.txt
- npm init Make sure you're here =>'frontend/'
- Node.JS installed on your computer.


### Sending Emails: 
Another feature of the application; is that you can send an email by entering your email; and clicking SendEmail; a basic plain text email is sent.
It is planned to supersede this to be a multi-part MIME message to allow rendering for other applications. 
<br>
Dynamic generation of HTML file containing the uploaded emails message headers. This goes to ```AnalysedHeaders.html``` under backend\eml_api 
#### CLI App:
How to manipulate mails on CLI:

`` python cli_app.py [OPTION] [FILE]``

Options:

Print the header from address ``` --hfrom /path/to/file.eml```

Print the header to address ```- -hto /path/to/file.eml ```

Print the subject of the Msg ``` --hsubject /path/to/file.eml```

Print the Reply-to address of the Msg ``` --hreply-to /path/to/file.eml```

Print the Msg ID of the Msg  ```--hmsg-id /path/to/file.eml ```

Print the date of the Msg:  ```--hdate /path/to/file.eml ```

Print the full Msg out: ``` --file /path/to/file.eml```

Create HTML file comprised of the attributes found in the eml : ```--makehtml /path/to/file.eml:``` * CLI generation of headers in a HTML file not possible yet.


#### Prerequisites: 
- Make sure that the ```SendEmailObjAttributes.json``` file under ```backend\email_functionality ``` has all the relevant fields filled...
  Don't fill the recipient one, It may be used for future purposes  in the application, so I'm keeping it.