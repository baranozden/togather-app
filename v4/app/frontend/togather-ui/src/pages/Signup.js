import FormSignup from '../components/FormSignup';
import React, { useState } from 'react';
import { BrowserRouter as Router, Routes, Route, Navigate } from "react-router-dom";


const Signup = () => {
    const [isSubmitted, setIsSubmitted] = useState(false);
    function submitForm() {
        setIsSubmitted(true);
    }
    return (
        <>
        <div className='form-container'>
            <div className='form-content-left'>
                <img className='form-img' src='images/signup-img.png' alt='togather-user' />
            </div>
            {!isSubmitted ? (
                <FormSignup submitForm={submitForm} />) : (<Navigate to ="/login" />
            )}
        </div>
        </>
    );
};

export default Signup;