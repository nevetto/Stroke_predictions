import React from "react";
import { Link } from "react-router-dom"
import "../styles/Navbar.css"
import images from "../styles/images";

// import { GiHamburgerMenu } from 'react-icons/gi';
// import { MdOutlineRestaurantMenu } from 'react-icons/md';

function Navbar () {
    const [toggleMenu, setToggleMenu] = React.useState(false);
    return(
        <nav className="app__navbar">
            <img src={images.stroke_doc } alt="stroke_doc"/>
            <ul className="app__navbar-links">
                <li > <Link className="navbar_items" to="/">Home </Link> </li>
                <li className="navbar_items"> <Link className="navbar_items" to="/login"> Login </Link> </li>
                <li className="navbar_items"> <Link className="navbar_items" to="/logout"> Logout </Link> </li>
                <li className="navbar_items"> <Link className="navbar_items" to="/register"> Register </Link></li>
            </ul>

            <div className="app__navbar-smallscreen">
                <div color="white" fontSize={27} onClick={() => setToggleMenu(true)}></div>
                {toggleMenu && (
                <div className="app__navbar-smallscreen_overlay flex__center slide-bottom">
                    <ul className="app__navbar-smallscreen_links">
                    <li><a href="#home" onClick={() => setToggleMenu(false)}>Home</a></li>
                    <li><a href="#login" onClick={() => setToggleMenu(false)}>Login</a></li>
                    <li><a href="#logout" onClick={() => setToggleMenu(false)}>Logout</a></li>
                    <li><a href="#register" onClick={() => setToggleMenu(false)}>Register</a></li>                    
                    </ul>
                </div>
                )}
            </div>
        </nav>
        
    )
}

export default Navbar;