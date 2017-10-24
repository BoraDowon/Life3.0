import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch'
import ApiUtils from "./ApiUtils";

class Home extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            posts: []
        }
    }

    componentDidMount() {
        let _this = this;
        fetch('/api/articles')
            .then(function (response) {
                return ApiUtils.parse(response)
            }).then(function (json) {
                _this.setState({posts: json['articles']})
        }).catch(function (ex) {
            console.log('api request failed!', ex)
        });
    }

    render() {
        const posts = this.state.posts.map((post) =>
            <li key={post['id']}>{post['title']}</li>
        );

        return (
            <div>
                <h1>Home react!!</h1>
                <ul>{posts}</ul>
            </div>
        )
    }
}

ReactDOM.render(
    <Home/>, document.getElementById('root')
)
