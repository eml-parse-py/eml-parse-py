import React from 'react';


const SendEmail = (props) => {


    return (
        <div>
            <label htmlFor="RcptEmail">Email to Send to: </label>
            <input
                type={"text"}
                name={"RcptEmail"}
                placeholder={"youremail@yourdomain.com"
                }
                onChange={props.validate}
            >
            </input>
            <button type="submit"
                    name={"SendEmail"}
                    onClick={props.clicked}
            >
                Send email
            </button>
        </div>
    );
}


export default SendEmail;