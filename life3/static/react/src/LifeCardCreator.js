import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch'
import ApiUtils from "./ApiUtils";

class LifeCardCreator extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            events: []
        }
    }

    componentDidMount() {
    }

    render() {
        return (
            <div>
                <button type="button" className="btn btn-success">Work</button>
                <button type="button" className="btn btn-info">Rest</button>
                <button type="button" className="btn btn-danger">Play</button>
                <br/>
                <label for="message">무슨 일을 하셨나요?</label>
                <input type="message" className="form-control" id="exampleInputEmail1" placeholder="Message"/>
                <button class="btn btn-default" type="submit">저장</button>
            </div>
        )
    }
}

export default LifeCardCreator;