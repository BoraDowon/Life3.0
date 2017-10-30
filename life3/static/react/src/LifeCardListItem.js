import React from 'react';
import 'whatwg-fetch'

class LifeCardListItem extends React.Component {

    constructor(props) {
        super(props);
    }

    render() {
        let typeIcon = null;
        if (this.props.cardType == 'W') {
            typeIcon = <span className="label label-success">&nbsp;&nbsp;&nbsp;</span>;
        } else if (this.props.cardType == 'R') {
            typeIcon = <span className="label label-info">&nbsp;&nbsp;&nbsp;</span>;
        } else {
            typeIcon = <span className="label label-danger">&nbsp;&nbsp;&nbsp;</span>;
        }

        return (
            <div className="life-card-padding">
                {typeIcon}
                <span className="life-card-title">{this.props.cardTitle}</span>
                <span className="life-card-date">{this.props.cardDate}</span>
            </div>
        )
    }
}

export default LifeCardListItem;