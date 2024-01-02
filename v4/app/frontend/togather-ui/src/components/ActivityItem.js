import { Button } from './Button';
import { Link } from "react-router-dom";
import React from "react";

import "./Activity.css"


function ActivityItem(props) {
    return (
        <li className="act__item">
            <Link className="act__item__link" to={props.path}>
                <figure className="act__item__pic-wrap">
                    <img src={props.picture} alt="img" className="act__item__img"/>
                </figure>
                <div className="act__item__info">
                    <h5 className="act__item__creds">
                        {props.first_name} {props.last_name} @{props.username}
                    </h5>
                    &nbsp;
                    <p className="act__item__text">
                        wants to be friend with you
                    </p>
                </div>
            </Link>
            <div className='act-btn'>
                <Link to="/signup" className="btn-mobile">
                    <Button
                    className="btns"
                    buttonStyle="btn--primary"
                    buttonSize="btn--medium"
                    >
                        Accept
                    </Button>
                </Link>
                &nbsp;
                &nbsp;
                &nbsp;
                &nbsp;
                <Link to="/signup" className="btn-mobile">
                    <Button
                    className="btns"
                    buttonStyle="btn--primary"
                    buttonSize="btn--medium"
                    >
                        Reject
                    </Button>
                </Link>
            </div>
        </li>
    )
}

export default ActivityItem;