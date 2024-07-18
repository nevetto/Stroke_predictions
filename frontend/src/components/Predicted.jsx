import React from "react";

function Predicted({pred, onDelete}){

    return(
        <div>
            <p>SEX: {pred.Male}</p>
            <p>USERNAME: {pred.username}</p>
            <p>RESULT: {pred.result}</p>
            <button className="delete-button" onClick={() => onDelete(pred.id)}>
                Delete
            </button>
        </div>
    );
}

export default Predicted