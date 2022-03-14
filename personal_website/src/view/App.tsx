import './App.css';
import { Routes, BrowserRouter, Route } from 'react-router-dom';
import NavBar from './nav/navbar';
import Home from './home/home';
import Login from '../apps/auth/login/login';
import Signup from '../apps/auth/signup/signup';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <NavBar />
        <Routes>
          <Route index element={<Home />} />
          <Route path='signup' element={<Signup />}/>
          <Route path='login' element={<Login />}/>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
