import { AiOutlineClose } from 'react-icons/ai';
import { FaBars } from 'react-icons/fa';
import { IconContext } from 'react-icons/lib';
import { Link } from 'react-router-dom';
import { NavbarData } from './NavbarData';
import React, { useEffect, useState } from 'react';

import './Navbar.css';

function Navbar() {
    const [sidebar, setSidebar] = useState(false)
    const showSidebar = () => setSidebar(!sidebar)

    const [isAuth, setIsAuth] = useState(false);
    useEffect(() => {
        if (localStorage.getItem('access_token') !== null) {
            setIsAuth(true); 
        }
    }, [isAuth]);
    
    return (
        <>
            <IconContext.Provider value={{ color: "#7b7b7b"}}>
                <div className="navbar">
                    <Link to="#" className="menu-bars">
                        <FaBars onClick={showSidebar}/>
                    </Link>
                    <h2 className="logo">togather</h2>
                </div>
                {isAuth ? 

                <nav className={sidebar ? "nav-menu active" : "nav-menu"}>
                    <ul className="nav-menu-items">
                        <li className="navbar-toggle">
                            <Link to="#" className="menu-bars">
                                <AiOutlineClose onClick={showSidebar}/>
                            </Link>
                            <h2 className="logo">togather</h2>
                        </li>

                        {NavbarData.map((item, index) => {
                            return (
                                <li key={index} className={item.cname}>
                                
                                <Link to={item.path}>
                                    {item.icon}
                                    <span>{item.title}</span>
                                </Link>
                                
                                </li>
                            )
                        })}

                    </ul>
                </nav>
                : null}
            </IconContext.Provider>
        </>
    )
}

export default Navbar;