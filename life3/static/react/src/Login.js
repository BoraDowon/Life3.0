import React from 'react';
import ReactDOM from 'react-dom';
import 'whatwg-fetch'
import ApiUtils from "./ApiUtils";

class Login extends React.Component {

    constructor(props) {
        super(props);

        this.facebookLogin = this.facebookLogin.bind(this);
        this.facebookLogout = this.facebookLogout.bind(this);
    }

    render() {
        return (
            <div className="login-area">
                <h1 className="header-title-font">Life 3.0</h1>
                <button className="fb-login-bt-custom" onClick={this.facebookLogin}>
                    <i className="fa fa-facebook"></i>
                    로그인 하기
                </button>
                <button className="fb-login-bt-custom" onClick={this.facebookLogout}>
                    <i className="fa fa-facebook"></i>
                    로그아웃 하기
                </button>
            </div>
        )
    }

    componentDidMount() {
        this.facebookSDKInit();
    }

    facebookSDKInit() {
        // Facebook SDK init
        let _this = this;
        window.fbAsyncInit = function () {
            FB.init({
                appId: '501258146921514',
                autoLogAppEvents: true,
                xfbml: true,
                version: 'v2.10'
            });
            _this.checkFacebookLoginStatus();
            //FB.AppEvents.logPageView();

        };

        (function (d, s, id) {
            var js, fjs = d.getElementsByTagName(s)[0];
            if (d.getElementById(id)) return;
            js = d.createElement(s);
            js.id = id;
            js.src = 'https://connect.facebook.net/ko_KR/sdk.js#xfbml=1&version=v2.10';
            fjs.parentNode.insertBefore(js, fjs);
        }(document, 'script', 'facebook-jssdk'));
    }

    checkFacebookLoginStatus() {
        FB.getLoginStatus(this.callbackForLoginStatus);
    }

    facebookLogin() {
        let _this = this;
        FB.login(function (response) {
            _this.checkFacebookLoginStatus();
        }, {scope: 'email,public_profile,user_friends'});
    }

    facebookLogout() {
        FB.logout(function(response) {
            console.log(response.status);
        });
    }

    callbackForLoginStatus(response) {
        console.log('status: ' + response.status);
        if (response.status == 'connected') {
            //console.log('accessToken: ' + response.authResponse.accessToken);
            //console.log('expiresIn: ' + response.authResponse.expiresIn);
            console.log('userID: ' + response.authResponse.userID);
            FB.api('/me', function (myResponse) {

                let _this = this;
                fetch('/login/api/auth/', {
                        method: 'POST',
                        headers: {'Content-Type': 'application/json'},
                        body: JSON.stringify({
                            userId: response.authResponse.userID,
                            userName: myResponse.name,
                            userEmail: myResponse.email,
                            accessToken: response.authResponse.accessToken,
                            type: "facebook"})})

                .then(function (response) {
                    return ApiUtils.parse(response)
                }).then(function (json) {
                    window.location = '/';
                }).catch(function (ex) {
                    console.log('api request failed!', ex)
                });
            });

        }
    }


}

ReactDOM.render(
    <Login/>, document.getElementById('root')
)