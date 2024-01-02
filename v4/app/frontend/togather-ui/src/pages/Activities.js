import ActivityItem from "../components/ActivityItem";
import React from "react";


function Activities() {
    return (
        <div className="activities">
            <h1>Activities</h1>
            <div className="acts__container">
                <div className="acts__wrapper">
                    <ul className="acts__items">
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        />
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        /> 
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        /> 
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        />
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        />
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        /> 
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        /> 
                        <ActivityItem 
                        picture="images/1.jpg"
                        first_name="John"
                        last_name="Dorian"
                        username="dorian"
                        path="/profile"
                        />      
                        
                    </ul>
                </div>
            </div>
        </div>
    )
}

export default Activities;