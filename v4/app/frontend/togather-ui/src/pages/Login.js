import FormLogin from '../components/FormLogin';
import React, { useState } from 'react';
import { Navigate } from "react-router-dom";


const Login = () => {
    const [isSubmitted, setIsSubmitted] = useState(false);
    function submitForm() {
        setIsSubmitted(true);
    }
    return (
        <>
        <div className='form-container'>
            <div className='form-content-left'>
                <img className='form-img' src='images/login-img.png' alt='spaceship' />
            </div>
            {!isSubmitted ? (
                <FormLogin submitForm={submitForm} />) : (<Navigate to ="/calendar" />
            )}
        </div>
        </>
    );
};

export default Login;