import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch'
import ApiUtils from "./ApiUtils";

import LifeCardCreator from "./LifeCardCreator";
import LifeCardListItem from "./LifeCardListItem";

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            events: []
        }
        this.refresh = this.refresh.bind(this);
        this.onCartCreated = this.onCartCreated.bind(this);
    }

    componentDidMount() {
        this.refresh();
    }

    refresh() {
        let _this = this;
        fetch('/api/lifecards')
            .then(function (response) {
                return ApiUtils.parse(response)
            }).then(function (json) {
                _this.setState({events: json['events']})
        }).catch(function (ex) {
            console.log('api request failed!', ex)
        });
    }

    onCartCreated() {
        this.refresh();
    }

    render() {
        const cards = this.state.events.map((event) =>
            <LifeCardListItem key={event['id']} cardId={event['id']} cardTitle={event['title']}
                              cardDate={event['time_to_display']} cardType={event['type']}/>
        );

        return (
            <div>
                <h1 className="header-title-font">Life 3.0</h1>
                <LifeCardCreator onCartCreated={this.onCartCreated}/>
                <div>{cards}</div>
            </div>
        )
    }
}

ReactDOM.render(
    <Home/>, document.getElementById('root')
)
