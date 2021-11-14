import React, { Component } from "react";
import { render } from "react-dom";
import HomeAn from "./AnComponents/HomeAn";

export default class App extends Component{
    constructor(props) {
        super(props)
    }


    render() {
        return (
            <div>
                <HomeAn/>
            </div>
        )
    }
}

const appDiv = document.getElementById("app");
render(<App/>, appDiv);