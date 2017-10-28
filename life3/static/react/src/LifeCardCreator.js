import React from 'react';
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
                <form className="form-inline">
                    <button type="button" className="btn btn-success">일</button>
                    <button type="button" className="btn btn-info">휴식</button>
                    <button type="button" className="btn btn-danger">놀이</button>
                    <input type="message" className="form-control" id="inputMessage" placeholder="간단한 설명"/>
                    <button className="btn btn-default" type="submit">저장</button>
                </form>

            </div>
        )
    }
}

export default LifeCardCreator;