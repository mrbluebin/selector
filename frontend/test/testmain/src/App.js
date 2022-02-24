import './App.css';
import RestAPI from "./RestAPI.js";
import React,{Component} from 'react';
import { Link, Route, Routes,BrowserRouter as Router } from 'react-router-dom'
import Mainpage from './page/Mainpage.js';
import Hello from './page/Hello'
import StartSelector from './page/Startselector';

function App() {

  return (
    <div>
      <Link to ='/'><button> HOME </button></Link>
    <Routes>
    
      <Route path="/" element={<Hello />} />
      <Route path="/menu" element={<Mainpage />} />
      <Route path="/selector/:name" element={<StartSelector />} />
    </Routes>
    </div>
  );
}
export default App;