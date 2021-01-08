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

Print the Reply-to address of the msg ``` --hreply-to /path/to/file.eml```

Print the Msg ID of the Msg  ```--hmsg-id /path/to/file.eml ```

Print the date of the Msg:  ```--hdate /path/to/file.eml ```

Print the full Msg out: ``` --file /path/to/file.eml```

Create HTML file comprised of the attributes found in the eml : ```--makehtml /path/to/file.eml:``` * Functionality is WIP.. 



## Technology stack in use:

- Python 3.7 minimum
- Flask API
- ReactJS for the Frontend rendering...


### Requirements:

- Python 3.7 or over.
- ReactJS 
- Flask API


## Installation:

- python -m pip install requirements.txt
- npm init Make sure you're here =>'eml-parse-py/web_app/react/app/static/parse_py_ui/'
- Node.JS installed on your device.

### To run:
- ```flask run ```
- If you've made changes make sure to run ```npm run build``` to get React changes updated, then re-run above.
