import React from 'react';
import 'whatwg-fetch'

class LifeCardListItem extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        let typeIcon = null;
        if (this.props.cardType == 'W') {
            typeIcon = <span className="label label-success">W</span>;
        } else if (this.props.cardType == 'R') {
            typeIcon = <span className="label label-info">R</span>;
        } else {
            typeIcon = <span className="label label-danger">P</span>;
        }
        let date = new Date(this.props.cardDate * 1000);
        // TODO: think more nice way to format it
        let formatted_date = date.toLocaleString().substring(0, date.toLocaleString().length-3);
        return (
            <div className="life-card-padding">
                {typeIcon}
                <span className="life-card-title">{this.props.cardTitle}</span>
                <span className="life-card-date">{formatted_date}</span>
            </div>
        )
    }
}

export default LifeCardListItem;