import React from 'react';
import axios from 'axios';
import SendEmail from "../smtp/SendEmail";
import Messagedata from "../msg/Messagedata";
import PreUploadMessageData from "../msg/PreUploadMessageData";
import './form.css';
import Form from 'react-bootstrap/Form';
import Button from 'react-bootstrap/Button';

class FormInput extends React.Component {


    constructor(props) {
        super(props);
        this.state = {
            file: null,
            msg_data: [],
            hasError: false,
            recipient: "",
            validated: false
        };
        this.onUploadHandler = this.onUploadHandler.bind(this)
        this.onSubmit = this.onSubmit.bind(this)
        this.handleEmailField = this.handleEmailField.bind(this)
        this.handleClickEmail = this.handleClickEmail.bind(this)

    }


    onUploadHandler(event) {

        this.setState({file: event.target.files[0]})
    }

    static getDerivedStateFromError(error) {
        // Update state so the next render will show the fallback UI.
        return {hasError: true};
    }


    componentDidCatch(error, errorInfo) {
        // You can also log the error to an error reporting service
        console.log(error, errorInfo);
    }

    onSubmit(event) {
        const formData = new FormData();
        event.preventDefault();


        formData.append("file", this.state.file, this.state.file.name);
        // formData.append('filename', );

        axios.post("/uploadfile", formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(
            (response) => {
                const res = response.data
                this.setState({file: res})

                axios.get("/fetchmetadata").then((response) => {
                        const result = response.data
                        this.setState({msg_data: result})
                    }
                );

            }).catch((error) => {
                if (error.response) {
                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                } else if (error.request) {
                    console.log(error.request);

                } else {
                    console.log('Error', error.message);

                }
            }
        );

    }

    handleEmailField(event) {
        if (event.target.value.match("^(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|" +
            "\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?" +
            "|\\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|" +
            "[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|" +
            "\\\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\\])$") != null && this.state.file != null) {
            this.setState({recipient: event.target.value});
        } else {
            this.render(
                <h1> Please upload and email before sending email.</h1>
            );
        }
    }


    handleClickEmail(event) {
        const formData = new FormData();
        event.preventDefault()
        formData.append(
            "text",
            this.state.recipient,
        );


        axios.post("/sendemail", formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(
            (response) => {
                const res = response.data.toString()
                console.log(res);
                this.setState({recipient: res})

            }).catch((error) => {
                if (error.response) {
                    console.log(error.response.data);
                    console.log(error.response.status);
                    console.log(error.response.headers);
                } else if (error.request) {
                    console.log(error.request);

                } else {
                    console.log('Error', error.message);

                }
            }
        );


    }


    render() {
        if (this.state.hasError) {

            return (
                <>
                    <h1> Whoops... Something went wrong.</h1>
                </>

            );
        } else {
            return (
                <div id={"file-input"}>

                    <h2 id={"App-heading"}> Eml Parse Py</h2>

                    <Form
                        validated={this.state.validate}
                        onSubmit={this.onSubmit}>

                        <Form.Group>
                            <Form.File
                                required
                                type={"file"}
                                accept="message/rfc822"
                                onChange={this.onUploadHandler}
                                feedback={"A file needs to be uploaded."}
                                id={"file_upload"}

                            >

                            </Form.File>


                            <Button
                                variant="success"
                                type="submit"
                                className={"uploadbutton"}
                            > Upload
                            </Button>
                            <PreUploadMessageData
                                file={this.state.file}/>
                            <Messagedata
                                msg_data={this.state.msg_data}/>
                        </Form.Group>
                        <SendEmail
                            clicked={this.handleClickEmail}
                            validate={this.handleEmailField}/>
                    </Form>


                </div>
            );
        }

    }

}


export default FormInput;
