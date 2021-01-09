import React from 'react';
import axios from 'axios';

class Form extends React.Component {
    constructor(props) {
        super(props);
        this.state = {
            file: null,
        };
        this.onUploadHandler = this.onUploadHandler.bind(this)
        this.handleClick = this.handleClick.bind(this)


    }

    onUploadHandler(event) {
        this.setState({file: event.target.files[0]})

    }


    handleClick(event) {
        const formData = new FormData();
        event.preventDefault();
        formData.append(
            this.state.file,
            this.state.file.name
        );

        axios.post("/uploadfile", formData).then(
            (response) => {
                const res = response.data
                console.log(res);
            }, (error) => {
                console.log(error);
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


    render() {
        return (
            <form>
                <input type="file" name="file" onChange={this.onUploadHandler}/>
                <button onClick={this.handleClick}> Upload</button>
                {this.fileInfo()}
            </form>
        );
    }

}


export default Form;
