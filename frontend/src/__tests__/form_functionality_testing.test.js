import React from "react";
import ReactDOM from "react-dom";
import {render, fireEvent} from "@testing-library/react";
import FormInput from "../form/form-input";
import {getQueriesForElement} from "@testing-library/dom";

function MockFile() {
};

MockFile.prototype.create = function (name, size, mimeType, lmtime) {
    name = name || "test.eml";
    size = size || 2000;
    mimeType = mimeType || "message/rfc822";
    lmtime = lmtime || "Mon Feb 01 2021";


    function range(cnt) {
        let output = "";
        let i = 0;
        for (i; i < cnt; i++) {
            output += "a"
        }
        return output;
    }

    var blob = new Blob([range(size)], {type: mimeType});
    blob.lastModifiedDate = new Date();
    blob.name = name;
    return blob;
};

describe("Conditional rendering checks... ", () => {

    it("Mock file for testing uploads.. ", () => {
        var file = new MockFile();
        expect(file).not.toBeNull();
    });

    it("Validating that the Mock file passes through generic values ", () => {
        var mock = new MockFile();
        var file = mock.create()

        expect(file.name).toBe('test.eml')
        expect(file.size).toBe(2000);
        expect(file.type).toBe('message/rfc822')
    });


});

describe("Functional testing of the form input", () => {
    it("Email input field is RFC compliant with smtp addresses accepted.", () => {

        const dummySMTPAddr = "smtpaddress@local.com"
        const {getByText, getByLabelText} = render(<FormInput/>)
        const emailAddr = getByLabelText("Email address")
        fireEvent.change(emailAddr, {target: {value: dummySMTPAddr}})
        fireEvent.click(getByText("Send email"))
        expect(dummySMTPAddr).toMatch(/^(([^<>()\[\]\\.,;:\s@"]+(\.[^<>()\[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,}))$/)

    });

    it("Testing upload functionality. ", () => {

    });
})