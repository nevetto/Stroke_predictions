import React from "react";
import "../styles/Home.css"

import images from "../styles/images";

import { Link } from "react-router-dom"

function Home() {
    return(
        <div className="home_container">
            <div className="home_bg_color">

                <div className="home_img_bg">
                <img src={images.stroke_img } alt="stroke_img"/>
                </div>

                <div className="home_fruit_img">
                    <img src={images.stroke_fruits} alt="stroke_fruits"/>
                    <div className="home_content"> 
                        <h3>What patient should avoid after having a stroke?</h3>
                        <div>Limit intake of foods containing saturated fat, added salt and added sugars: Limit foods high in saturated fat such as biscuits, cakes, pastries, pies, processed meats, commercial burgers, pizza, fried foods, potato chips, crisps and other savoury snacks. </div>

                        <h3>What is the best food for a stroke patient?</h3>
                        <div>Eat a heart-healthy diet: A diet that supports heart health is also important for stroke recovery. This includes plenty of fruits, vegetables, whole grains, lean proteins (like fish, poultry, beans, and nuts), and healthy fats (found in avocados, olive oil, nuts, and seeds). </div>
                    </div>
                </div>
            </div>

            <p className="home_link"><h2 className="home_content"> Health, they say is wealth. To predict posibility of stroke <span><Link to="/register"> Register </Link>/<Link to="/login"> Login </Link></span></h2> </p>
        </div>
        
    )
    
}
export default Home;