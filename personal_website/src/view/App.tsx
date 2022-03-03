import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Feed } from './feed/feed';

function App() {
  return (
    <div className="App">
      <h1>
        Feed header
      </h1>
      <Feed />
    </div>
  );
}

export default App;
