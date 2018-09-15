import React, { Component } from 'react';
import './App.css';

const API = 'http://127.0.0.1:5000/article?url=';
const query = encodeURIComponent(window.location.href);

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      content: (
        <div className="loading">News Articles Loading</div>
      ),
    };
  }

  render() {
    	fetch(API + query)
      .then(response => console.log(JSON.stringify(response.json())));

    return (
      <div className="App">
        {this.state.content}
      </div>
    );
  }
}

export default App;
