import React from "react";

function Predicted({pred}){

    return(
        <div>
            <p>{pred.first_name}</p>
            <p>{pred.second_name}</p>
            <p>{pred.result}</p>
        </div>
    );
}

export default Predicted