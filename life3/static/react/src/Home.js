import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch'
import ApiUtils from "./ApiUtils";

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            events: []
        }
    }

    componentDidMount() {
        let _this = this;
        fetch('/api/life-logs')
            .then(function (response) {
                return ApiUtils.parse(response)
            }).then(function (json) {
                _this.setState({events: json['events']})
        }).catch(function (ex) {
            console.log('api request failed!', ex)
        });
    }

    render() {
        const posts = this.state.events.map((event) =>
            // FIXME: insert right key
            <li>{event['title']}, {event['type']}, {event['timestamp']}</li>
        );

        return (
            <div>
                <h1>Life 3.0</h1>
                <ul>{posts}</ul>
            </div>
        )
    }
}

ReactDOM.render(
    <Home/>, document.getElementById('root')
)
