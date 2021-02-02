import React from 'react';


const preFileInfo = (props) => {

    if (props.file) {
        return (
            <div>
                <h4>File Details:</h4>
                <p>File Name: {props.file.name}</p>
                <p>Content type / MIME Type: {props.file.type}</p>
                <p>
                    Last Modified:{" "}
                    {props.file.lastModifiedDate.toDateString()}
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

export default preFileInfo;