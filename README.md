# Eml Parse Py 

## A web based SMTP analysis tool that parses mail into a HTML file; and is attached to an email for reporting purposes.

## Tech stack in use:

- Python 3.8
- ReactJS 

# Installation:

- python -m pip install requirements.txt
- npm init Make sure you're here =>'frontend/'
- Node.JS installed on your computer.

# How to use:

## To run Web application:
#### BACKEND: 

```
 
Create an environment variable 
Windows:
set / export  FLASK_APP=app.py <- This lets the below command "flask run" work.
set / export FLASK_ENV=development <- This sets the app to debug mode 

flask run

For reference:

export for *NIX systems/ MAC OS, and set for Windows
```

#### FRONTEND 

```
Start the application:
npm start 
```

#### Prerequisites: 
- Ensure to populate ```SendEmailObjAttributes.json``` file under ```  backend\email_functionality``` omit the recipient field as user input is used, and I plan to use this field for something else in the future.


## CLI options

Navigate to ```backend/eml_api/cli_app.py``` to use these options.

Options:

Print the header from address ``` --hfrom /path/to/file.eml```

Print the header to address ```- -hto /path/to/file.eml ```

Print the subject of the Msg ``` --hsubject /path/to/file.eml```

Print the Reply-to address of the Msg ``` --hreply-to /path/to/file.eml```

Print the Msg ID of the Msg  ```--hmsg-id /path/to/file.eml ```

Print the date of the Msg:  ```--hdate /path/to/file.eml ```

Print the full Msg out: ``` --file /path/to/file.eml```

Create HTML file comprised of the attributes found in the eml : ```--makehtml /path/to/file.eml:``` * CLI header generation to be added, web based is only possible at this time.
