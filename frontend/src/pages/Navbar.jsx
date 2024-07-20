import { Link } from "react-router-dom"
import "../styles/Navbar.css"
import images from "../styles/images";

function Navbar () {
    return(
        <nav className="app__navbar">
            <img src={images.stroke_doc } alt="stroke_doc"/>
            <ul className="app__navbar-links">
                <li className="p__opensans"> <Link to="/">Home </Link> </li>
                <li className="p__opensans"> <Link to="/login"> Login </Link> </li>
                <li className="p__opensans"> <Link to="/logout"> Logout </Link> </li>
                <li className="p__opensans"> <Link to="/register"> Register </Link></li>
            </ul>
        </nav>
        
    )
}

export default Navbar;