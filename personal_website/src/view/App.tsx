import React from 'react';
import logo from './logo.svg';
import './App.css';
import { Feed } from './feed/feed';

function App() {
  return (
    <div className="App">
      <h1>
        Feed header

        Sam Whelan, Simon Gairing, Benjamin Sharp, Brendon Kenny, Anthony S, Tony B, Micheala Kenny, Dwayne The Rock Johnson, Taylor Atherton, Hannah Atherton, Kate Whelen, Emma Whelen, Andy Whelan  
      </h1>
      <Feed />
    </div>
  );
}

export default App;
