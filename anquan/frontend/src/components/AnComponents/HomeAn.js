import React, { Component } from "react";
import AnHeader from "./AnHeader";

export default class HomeAn extends Component {
    constructor(props) {
        super(props)
        this.state = {
            headerName: "Home",
        }
    }

    render() {
        return (
            <div>
                <AnHeader headerName={this.state} />
            </div>
        )
    }
}