import React from 'react';
import axios from 'axios';
import SendEmail from "../smtp/SendEmail";

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null,
            msg_data: [],
            hasError: false,
            recipient: ""
        };
        this.onUploadHandler = this.onUploadHandler.bind(this)
        this.handleClick = this.handleClick.bind(this)
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

    handleClick(event) {
        const formData = new FormData();
        event.preventDefault();
        formData.append(
            "file",
            this.state.file,
            this.state.file.name
        );

        axios.post("/uploadfile", formData, {
            headers: {
                'Content-Type': 'multipart/form-data'
            }
        }).then(
            (response) => {
                const res = response.data
                console.log(res);
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
        this.setState({
            recipient: event.target.value
        });
    }

    fileInfo() {

        if (this.state.file) {
            return (
                <div>
                    <h4>File Details:</h4>
                    <p>File Name: {this.state.file.name}</p>
                    <p>Content type / MIME Type: {this.state.file.type}</p>
                    <p>
                        Last Modified:{" "}
                        {this.state.file.lastModifiedDate.toDateString()}
                    </p>
                </div>
            );
        } else {
            return (
                <div>
                    <br/>
                    <h4>Upload a file before clicking upload</h4>
                </div>
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
                // this.setState({recipient: res})

            })



    }


    msg_Data() {

        return (
            <div id={"msg-headers"}>
                {(this.state.msg_data || []).map(item => (

                    <ul key={item}>
                        <ul> {item[0]}: {item[1]}</ul>
                    </ul>)
                )}
                <br/>

            </div>

        );

    }


    render() {
        if (this.state.hasError) {

            return (
                <div>
                    <h1> Whoops... Something went wrong.</h1>

                </div>

            );
        } else {
            return (
                <div>
                    <form>

                        <input type="file" name="file" required={"file"} onChange={this.onUploadHandler}
                               accept="message/rfc822"/>
                        <button type="submit" onClick={this.handleClick}> Upload</button>
                        {this.fileInfo()}
                        {this.msg_Data()}

                    </form>
                    <SendEmail name={this.handleEmailField}
                               clicked={this.handleClickEmail}/>
                </div>
            );
        }

    }

}


export default Form;
