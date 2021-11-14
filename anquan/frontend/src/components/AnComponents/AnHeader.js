import React, { Component } from "react";

export default class AnHeader extends Component {
    constructor(props) {
        super(props)
    }

    render() {
        return (
            <div className="an-header">
                <div className="d-flex align-items-center">
                    <p>Back</p>
                </div>
                <div className="d-flex justify-content-center align-items-center">
                    <h4 className="mx-2">{headerName}</h4>
                </div>
            </div>
        );
    }
}