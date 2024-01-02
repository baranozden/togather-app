import { Button } from './Button';
import { CiLocationOn } from "react-icons/ci";
import { Link } from "react-router-dom";
import React from "react";


function BrowseCardItem(props) {
    return (
        <li className="cards__item">
            <Link className="cards__item__link" to={props.path}>
                <figure className="cards__item__pic-wrap">
                    <img src={props.picture} alt="img" className="cards__item__img"/>
                </figure>
                <div className="cards__item__info">
                    <h5 className="cards__item__creds">
                        {props.first_name} {props.last_name} @{props.username}
                    </h5>
                    <p className="cards__item__interest">
                        Interested with {props.interest}
                    </p>
                    <p className="cards__item__location">
                        <CiLocationOn />
                        {props.city}
                    </p>
                </div>
            </Link>
            <div className='card-btn'>
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
        </li>
    )
}

export default BrowseCardItem;