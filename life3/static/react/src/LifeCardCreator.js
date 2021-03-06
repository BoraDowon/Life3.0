import React from 'react';
import 'whatwg-fetch'
import ApiUtils from "./ApiUtils";

class LifeCardCreator extends React.Component {

    constructor(props) {
        super(props);
        this.state = {
            selected_type: null,
            typed_message: '',
            warning_message: ''
        }
    }

    onClickWorkButton() {
        this.setState({selected_type: 'W'});
    }

    onClickPlayButton() {
        this.setState({selected_type: 'P'});
    }

    onClickRestButton() {
        this.setState({selected_type: 'R'});
    }

    onChangeMessageInput(e) {
        this.setState({typed_message: e.target.value})
    }

    submitButtonClick() {
        if (this.state.selected_type == null) {
            this.setState({warning_message: '타입을 먼저 선택해주세요!'})
            return;
        }

        if (this.state.typed_message == '') {
            this.setState({warning_message: '내용을 입력해주세요!'})
            return;
        }

        let _this = this;
        fetch('/dashboard/api/lifecards/', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({
                title: this.state.typed_message,
                type: this.state.selected_type,
                timestamp: new Date().getTime() / 1000
            })
        })
        .then(function (response) {
            return ApiUtils.parse(response)})
        .then(function (json) {
            if (json['result'] != 'success') {
                _this.setState({warning_message: '네트워크가 현재 원활하지 않습니다!'});
            } else {
                _this.setState({selected_type: null, typed_message: '', warning_message: ''})
                _this.props.onCartCreated();
            }
        }).catch(function (ex) {
            _this.setState({warning_message: '통신 도중 서버 에러가 발생 했습니다!'});
        });
    }

    render() {
        return (
            <div claaName="wrap-form">
                <div className="form-inline">
                    <button type="button" className={this.state.selected_type === "W" ? "btn btn-w selected" : "btn btn-w"} onClick={() => this.onClickWorkButton()}>일</button>
                    <button type="button" className={this.state.selected_type === "R" ? "btn btn-r selected" : "btn btn-r"} onClick={() => this.onClickRestButton()}>휴식</button>
                    <button type="button" className={this.state.selected_type === "P" ? "btn btn-p selected" : "btn btn-p"} onClick={() => this.onClickPlayButton()}>놀이</button>
                </div>
                <div className="input-group">
                    <input type="message" className="form-control" id="inputMessage" placeholder="간단한 설명"
                         onChange={(e) => this.onChangeMessageInput(e)} value={this.state.typed_message}/>
                    <span className="input-group-btn">
                      <button className="btn btn-default" onClick={(e) => this.submitButtonClick(e)}>저장</button>
                    </span>
                </div>
                <p className="bg-danger">{this.state.warning_message}</p>
            </div>
        )
    }
}

export default LifeCardCreator;
