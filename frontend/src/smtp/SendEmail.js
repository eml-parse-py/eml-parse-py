import React from 'react';
import Form from 'react-bootstrap/Form'

import Button from 'react-bootstrap/Button';
import './SendEmail.css';

const SendEmail = (props) => {


    return (

        <div id={"Email-form"}>

            <Form.Group>
                <Form.Label> Email address</Form.Label>
                <Form.Control.Feedback
                    feedback="An email must be provided."
                    required>

                </Form.Control.Feedback>
                <Form.Control type="email" placeholder="yourmail@domain.com"
                              required
                              onChange={props.validate}/>

            </Form.Group>

            <Button
                variant="success"
                type="submit"
                name={"SendEmail"}
                onClick={props.clicked}
            >
                Send email
            </Button>
        </div>
    );
}


export default SendEmail;