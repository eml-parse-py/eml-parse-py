# eml-parse-py

## Purpose:
A CLI based SMTP Message analysis tool, for things such as parsing individual entities, and constructing reports, and sending them via another SMTP message *



SMTP message sending functionality planned... * 


## How to use:

How to manipulate mails on CLI:

`` python app.py [OPTION] [FILE]``

Options:

Print the header from address ``` --hfrom /path/to/file.eml```

Print the header to address ```- -hto /path/to/file.eml ```

Print the subject of the Msg ``` --hsubject /path/to/file.eml```

Print the Reply-to address of the Msg ``` --hreply-to /path/to/file.eml```

Print the Msg ID of the Msg  ```--hmsg-id /path/to/file.eml ```

Print the date of the Msg:  ```--hdate /path/to/file.eml ```

Print the full Msg out: ``` --file /path/to/file.eml```

Create HTML file comprised of the attributes found in the eml : ```--makehtml /path/to/file.eml:``` * Functionality is WIP.. 



## Technology stack in use:

- Python 3.7 minimum
- Flask API (this is backend of the system)
- ReactJS for the Frontend rendering...


### Requirements:

- Python at least 3.8
- ReactJS 
- Flask API


## Installation:

- python -m pip install requirements.txt
- npm init Make sure you're here =>'eml-parse-py/web_app/react/app/static/parse_py_ui/'
- Node.JS installed on your device.

### To run:
- ```flask run ```
- ```npm run ``` this is the ReactJS  frontend

### Sending Emails: 
Another feature of the application; is that you can send an email by entering your email; and clicking SendEmail; a basic plain text email is sent.
It is planned to supersede this to be a multi-part MIME message to allow rendering for other applications. 
<br>
 HTML file comprimising of a messages headeres is planned... The current ```test.html``` in use is placeholder for now, and will be superseded by a file named headers.html which will contain a nicely styled HTML file containing the headers.
#### Pre-requesites: 
- Make sure that the ```SendEmailObjAttributes.json``` file under ```Flask\email_functionality ``` has all the relevant fields filled... Don't fill the recipient one, It may be used for future purposes  in the application so I'm keeping it.


