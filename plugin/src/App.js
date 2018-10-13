/*global chrome*/
import React, { Component } from 'react';
import './App.css';
import { default as _map } from 'lodash/map';

const API = 'http://127.0.0.1:5000/article?url=';

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      content: (
        <div className="loading">News Articles Loading</div>
      ),
      url: '',
      request: 0,
    };
  }

  render() {
    console.log(this.state.request);
    let articles = [];
    if (this.state.url === '') {
      chrome.tabs.query({'active': true, 'windowId': chrome.windows.WINDOW_ID_CURRENT},
        (tabs) => {
          this.setState({ url: encodeURIComponent(tabs[0].url) })
        }
      );
    } else if (!Array.isArray(this.state.content) && this.state.request === 0) {
      fetch(API + this.state.url)
        .then(response => response.json())
        .then(result => this.setState({ content: result }));
      this.setState({ request: 1 });
    }

    console.log(this.state.content);

    if(Array.isArray(this.state.content)) {
      articles = _map(
        this.state.content,
        (item, index) => {
          console.log(this.state.content);
          if (index === this.state.content.length - 1) {
            return (
              <div>
                <p><a href={item.url}>{item.title}</a></p>
                <img src={item.image} width="150" />
              </div>
            );
          }
          return (
            <div>
              <p><a href={item.url}>{item.title}</a></p>
              <img src={item.image} width="150" />
              <hr />
            </div>
          );
        }
      );
    }

    const regex = new RegExp('.*(thestar.com|torontosun.com)/(news|opinion|life|entertainment|sports).*');

    let popupContent;
    if(this.state.url === '') {
      popupContent = this.state.content;
    } else if (!regex.test(decodeURIComponent(this.state.url))) {
      popupContent = 'Extension not current available.'
    } else if (Array.isArray(this.state.content)) {
      popupContent = articles;
    }

    return (
      <div className="App">
        {popupContent}
      </div>
    );
  }
}

export default App;
