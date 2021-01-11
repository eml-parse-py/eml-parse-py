import React from 'react';
import axios from 'axios';

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null,
            msg_data: [],
            hasError: false
        };
        this.onUploadHandler = this.onUploadHandler.bind(this)
        this.handleClick = this.handleClick.bind(this)


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


    msg_Data() {
        if (this.state.msg_data) {
            return (
                <div>
                    <p>
                        Message headers: <br/>{this.state.msg_data}
                    </p>
                </div>

            );
        } else {
            return (
                <div>
                    <p> Insert a file above </p>
                </div>
            );
        }
    }


    render() {
        if (this.state.hasError) {
            // You can render any custom fallback UI
            return <h1>Something went wrong.</h1>;
        }
        return (
            <form>
                <input type="file" name="file" onChange={this.onUploadHandler} accept="message/rfc822"/>
                <button onClick={this.handleClick}> Upload</button>
                {this.fileInfo()}
                {this.msg_Data()}
            </form>
        );
    }

}


export default Form;
