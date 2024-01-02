import { BrowserRouter as Router, Routes, Route} from 'react-router-dom';
import React, { useState } from "react";

import Activities from './pages/Activities';
import Browse from './pages/Browse';
import Calendars from './pages/Calendars';
import Communities from './pages/Communities';
import Friends from './pages/Friends';
import Landing from './pages/Landing';
import Login from './pages/Login';
import Logout from './components/Logout';
import Navbar from './components/Navbar';
import Profile from './pages/Profile';
import SetProfile from './pages/SetProfile';
import Signup from './pages/Signup';


import "react-big-calendar/lib/css/react-big-calendar.css";
import "react-datepicker/dist/react-datepicker.css";
import "./App.css";


function App() {
  return (
    <div className="App">
      <Router>
        <Navbar />
        <Routes>
          <Route path="/calendar" element={<Calendars />}/>
          <Route path="/signup" element={<Signup />}/>
          <Route path="/login" element={<Login />}/>
          <Route path="/logout" element={<Logout />}/>
          <Route path="/setprofile" element={<SetProfile />}/>
          <Route path="/starting" element={<Landing />}/>
          <Route path="/browse" element={<Browse />}/>
          <Route path="/profile" element={<Profile />}/>
          <Route path="/activity" element={<Activities />}/>
          <Route path="/friends" element={<Friends />}/>
          <Route path="/communities" element={<Communities />}/>
        </Routes>
      </Router>
      
    </div>
  );
}

export default App;