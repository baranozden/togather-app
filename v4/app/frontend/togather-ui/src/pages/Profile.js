import { Button } from '../components/Button';
import { CiLocationOn } from "react-icons/ci";
import { Link } from "react-router-dom";
import React from "react";


function Profile() {
    return (
        <div className="profile">
            <figure className="profile__pic-wrap">
                <img src="images/1.jpg" alt="img" className="profile__img"/>
            </figure>
            <div className="profile__info">
                <h3 className="profile__creds">
                    John Dorian @dorian
                </h3>

                <p className="profile__location">
                    <CiLocationOn />
                    Ankara
                </p>

                <p className="profile__interest">
                    Interested with music
                </p>

                <p className="profile__interest">
                    Bio: This person does not exist.
                </p>

                <p className="profile__interest">
                    13.10.1995
                </p>
                
            </div>
            
            <div className='profile-btn'>
                <Link to="/signup" className="btn-mobile">
                    <Button
                    className="btns"
                    buttonStyle="btn--primary"
                    buttonSize="btn--medium"
                    >
                        Add Friend
                    </Button>
                </Link>
            </div>
        </div>
    )
}

export default Profile;