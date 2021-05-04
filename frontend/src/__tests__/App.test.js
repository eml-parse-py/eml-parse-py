import React from "react";
import App from "../form/App";
import {shallow} from "enzyme";
import FormInput from "../form/form-input";
import Button from "react-bootstrap/Button";
import SendEmail from "../smtp/SendEmail";


describe("Ensuring components render as intended.", () => {
    it("Render the app without crashing", () => {
        shallow(<App/>)
    });

    it("App's component header renders without crashing... ", () => {
        const wrapper = shallow(<App/>);
        const header = (<h2 id={"App-heading"}> Eml Parse Py</h2>);
        expect(wrapper.contains(header)).toEqual(true);
    });

    it("Rendering the FormInput Component ", () => {
        shallow(<FormInput/>)
    });
    it("Rendering the Upload button", () => {
        const wrapper = shallow(<FormInput/>);
        const button = (
            <Button
                variant="success"
                type="submit"
                className={"uploadbutton"}
            > Upload
            </Button>
        )
        expect(wrapper.contains(button)).toEqual(true)
    });

    it("Send Email component renders",()=>{
        shallow(<SendEmail/>);
    })


});