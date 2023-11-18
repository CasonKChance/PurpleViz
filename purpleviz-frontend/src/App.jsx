import React, {useState} from 'react';
import './App.css';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import MainComponent from './pages/MainComponent';
import CameraComponent from './pages/CameraComponent';
function App() {
  return (
    <Router>
    <Routes>
        <Route path="/" element={<MainComponent />} />
        <Route path="/camera" element={<CameraComponent />} />
    </Routes>
    </Router>
  )
}


export default App;
