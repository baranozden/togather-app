import React from "react";
import FriendCardItem from "./FriendCardItem";

import "./Cards.css";

function FriendCards() {
    return (
        <div className="cards">
            <div className="cards__container">
                <div className="cards__wrapper">
                    <ul className="cards__items">
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        />
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        /> 
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        /> 
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        /> 
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        /> 
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        /> 
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        /> 
                        <FriendCardItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        interest="music"
                        city="ankara"
                        path="/calendars"
                        />                   
                        
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default FriendCards;