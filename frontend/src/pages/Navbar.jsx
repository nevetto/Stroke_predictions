import { Link } from "react-router-dom"
import "../styles/Navbar.css"

function Navbar () {
    return(
        <nav className="app__navbar">
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