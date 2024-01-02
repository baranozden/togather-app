import { Button } from '../components/Button';
import { useNavigate } from "react-router";
import React from 'react';



function Landing() {
    let navigate = useNavigate();
    function handleClickSignup() {
        navigate("/signup");
    };
    function handleClickLogin() {
        navigate("/login");
    };

    return (
        <div className='landing'>
            <h1>Be Professional, Be Social</h1>
            <p>
                ToGather is a next generation automated and intelligent social calendar application. 
                This application provides an all-in-one solution for managing professional and social life with ease. 
            </p>
            <div className='landing-btns'>
                <Button
                className="btns"
                buttonStyle="btn--outline"
                buttonSize="btn--large"
                onClick={handleClickSignup}
                >
                    Signup
                </Button>
                <Button
                className="btns"
                buttonStyle="btn--primary"
                buttonSize="btn--large"
                onClick={handleClickLogin}
                >
                    Login
                </Button>
            </div>
        </div>
    )
}

export default Landing;