import React from 'react'
import { useState, useEffect } from "react";
import Predicted from '../components/Predicted';
import api from "../api";


function Predict() { 
    

    const [getPred, setgetPred] = useState([]);  
    
   
    const [first_name, setFirst_name] = useState('');
    const [second_name, setSecond_name] =useState('');
    const [Male, setMale] =useState("");
    const [Female, setFemale] =useState("");
    const [ever_married, setEver_married] = useState("");
    const [Not_married, setNot_married] =useState("");
    const [Govt_job, setGovt_job] =useState("");
    const [Private, setPrivate] =useState("");
    const [Self_employed, setSelf_employed] =useState("");
    const [children, setChildren] =useState("");
    const [Rural, setRural] =useState("");
    const [Urban, setUrban] =useState("");
    const [Unknown_smoke, setUnknown_smoke] =useState("");
    const [formerly_smoked, setformerly_smoked] =useState("");
    const [never_smoked, setnever_smoked] =useState("");
    const [smokes, setSmokes] =useState("");
    const [age, setAge] =useState(0);
    const [hypertension, setHypertension] =useState(0);
    const [heart_disease, setHeart_disease] =useState(0);
    const [avg_glucose_level, setAvg_glucose_level] =useState(0);
    const [bmi, setBmi] =useState(0);
     


    

    useEffect(()=> {
        getPredicts();
    }, []);

    const getPredicts = () => {
        api.get("/predictions/predict/")
        .then((res) => res.data)
        .then((data) => {
            setgetPred(data);
            console.log(data);
        })
        .catch((err) => alert(err));
    };

    const createPredicts = (e) => {
      e.preventDefault();
      api.post("/predictions/predict/", { first_name,second_name,Male,Female, ever_married,Not_married, Govt_job, Private, Self_employed, children, Rural,
        Urban, Unknown_smoke,formerly_smoked,never_smoked,smokes, age,hypertension,heart_disease,avg_glucose_level, bmi }).then((res) => {
          if (res.status === 201) alert("Your Information Has Been Successfully Sent.");
          else alert("Failed to make prediction.");
          getPredicts();
        })
        .catch((err) => alert(err));
        // .catch((err) =>console.log(err + data))         
    };

  

     
  return (
    <div>
       
      <div>
        <div>
          <h2>Predictions</h2>
          { getPred.map((pred) => (
            <Predicted pred={pred} key={pred.first_name} secondN={pred.second_name} result = {pred.result}/>
          ))}
           
        </div>
        <h2>Make Predictions</h2>
         <form onSubmit={createPredicts}>
          <label htmlFor="first_name">First Name</label>
          <input
              type="text"
              id="first_name"
              name="first_name"
              required
              onChange={(e) => setFirst_name(e.target.value)}
              value={first_name}
          />
          <label htmlFor='second_name'>Second Name</label>
          <input
              type="text"
              id="second_name"
              name="second_name"
              required
              onChange={(e) => setSecond_name(e.target.value)}
              value={second_name}
          />          
          <h2>Sex Note: Select Yes</h2>
          <div>
          <label>Male</label>
            
            <input
            type='text'
            placeholder='Select Button'
            id="Male"
            name='Male'
            onChange={(e) => setMale(e.target.value)}
            value={Male}
                       
            />

            {Male == "" ? 
                <span><input type='button'onClick={()=> setMale("Male")} />Yes</span>
                : 
                 <span><input type='button'  onClick={()=> setMale("")} />No </span>
                
            }

          </div>

          <br></br>
            

          <label htmlFor='Female'>Female</label>
            <input
             
            id="Female"
            name='Female'
            onChange={(e) => setFemale(e.target.value)}
            value={Female}
            
            />
            {Female == "" ? 
            <span><input type='button' onClick={()=> setFemale("Female")}/>Yes</span> 
            : 
            <span><input type='button' onClick={()=> setFemale("")}/>No</span> 
            
          }
            
          <h2>Marrital Status</h2>
          <label htmlFor='ever_married'>Married</label>
            
          
            <input
             
            id="ever_married"
            name='ever_married'
            onChange={(e) => setEver_married(e.target.value)}
            value={ever_married}
            ever_married
            />
            {ever_married == "" ? 
            <span><input type='button' onClick={()=> setEver_married("ever_married")}/>Yes</span> 
            : 
            <span><input type='button' onClick={()=> setEver_married("")}/>No</span>
            
          }

          <label htmlFor='Not_married'>Not Married</label>
            <input            
            id="Not_married"
            name='Not_married'
            onChange={(e) => setNot_married(e.target.value)}
            value={Not_married}
            
            />
            {Not_married == "" ? 
            <span><input type='button' onClick={()=> setNot_married("Not_married")}/>Yes</span> 
            :
            <span><input type='button' onClick={()=> setNot_married("")}/>No</span>            
            }
 
          <h2>Employment Type</h2>
          <label htmlFor='Govt_job'>Government Worker</label>
            <input            
            id="Govt_job"
            name='Govt_job'
            onChange={(e) => setGovt_job(e.target.value)}
            value={Govt_job}
            
            />
            {Govt_job == "" ? 
            <span> <input type='button' onClick={()=> setGovt_job( "Govt_job")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setGovt_job("")}/>No</span>            
            }

         <label htmlFor='Private'>Private Worker</label>
            <input            
            id="Private"
            name='Private'
            onChange={(e) => setPrivate(e.target.value)}
            value={Private}
            Private
            />
            {Private == "" ? 
            <span><input type='button' onClick={()=> setPrivate("Private")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setPrivate("")}/>No</span>
            
          }

          <label htmlFor='Self_employed'>Self Employed</label>
            <input            
            id="Self_employed"
            name='Self_employed'
            onChange={(e) => setSelf_employed(e.target.value)}
            value={Self_employed}
            Self_employed
            />
            {Self_employed == "" ? 
            <span><input type='button' onClick={()=> setSelf_employed("Self_employed")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setSelf_employed("")}/>No</span>
            
          }

          <label htmlFor='children'>Children</label>
            <input            
            id="children"
            name='children'
            onChange={(e) => setChildren(e.target.value)}
            value={children}
            />
            {children == "" ? 
            <span><input type='button' onClick={()=> setChildren("children")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setChildren("")}/>No</span>
            
          }

          <h2>Residence Area</h2>
          <label htmlFor='Rural'>Rural</label>
            <input            
            id="Rural"
            name='Rural'
            onChange={(e) => setRural(e.target.value)}
            value={Rural}
            Rural
            />
            {Rural == "" ? 
            <span><input type='button' onClick={()=> setRural("Rural")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setRural("")}/>No</span>
            
          }

          <label htmlFor='Urban' >Urban</label>
            <input            
            id="Urban"
            name='Urban'
            onChange={(e) => setUrban(e.target.value)}
            value={Urban}
            Urban
            />
            {Urban == "" ? 
            <span><input type='button' onClick={()=> setUrban("Urban")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setUrban("")}/>No</span>            
            }

          <h2>Smoking Status</h2>
          <label htmlFor='Unknown_smoke' >Unknown Smoker</label>
            <input            
            id="Unknown_smoke"
            name='Unknown_smoke'
            onChange={(e) => setUnknown_smoke(e.target.value)}
            value={Unknown_smoke}
            Unknown_smoke
            />
            {Unknown_smoke == "" ? 
            <span><input type='button' onClick={()=> setUnknown_smoke("Unknown_smoke")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setUnknown_smoke("")}/>No</span>            
            }

          <label htmlFor='formerly_smoked' >formerly Smoked</label>
            <input            
            id="formerly_smoked"
            name='formerly_smoked'
            onChange={(e) => setformerly_smoked(e.target.value)}
            value={formerly_smoked}
            formerly_smoked
            />
            {formerly_smoked == "" ? 
            <span><input type='button' onClick={()=> setformerly_smoked("formerly_smoked")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setformerly_smoked("")}/>No</span>            
            }

          <label htmlFor='never_smoked'>Never Smoked</label>
            <input            
            id="never_smoked"
            name='never_smoked'
            onChange={(e) => setnever_smoked(e.target.value)}
            value={never_smoked}
            
            />
            {never_smoked == "" ? 
            <span><input type='button' onClick={()=> setnever_smoked("never_smoked")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setnever_smoked("")}/>No</span>            
            }

          <label htmlFor="smokes">smokes</label>
          <input
              type="text"
              id="smokes"
              name="smokes"
              required
              onChange={(e) => setSmokes(e.target.value)}
              value={smokes}
          />

          {smokes == "" ? 
            <span><input type='button' onClick={()=> setSmokes("smokes")}/>Yes</span>
            : 
            <span><input type='button' onClick={()=> setSmokes("")}/>No</span>            
            }

          <label>Age</label>
          <input
              type="number"
              id="age"
              name="age"
              required
              onChange={(e) => setAge(e.target.value)}
              value={age}
          />

          <label>Hypertension</label>
          <input
              type="number"
              id="hypertension"
              name="hypertension"
              required
              onChange={(e) => setHypertension(e.target.value)}
              value={hypertension}
          />

        
          <label>Heart Disease</label>
          <input
              type="number"
              id="heart_disease"
              name="heart_disease"
              required
              onChange={(e) => setHeart_disease(e.target.value)}
              value={heart_disease}
          />

          <label>Average Glucose Level</label>
          <input
              type="number"
              id="avg_glucose_level"
              name="avg_glucose_level"
              required
              onChange={(e) => setAvg_glucose_level(e.target.value)}
              value={avg_glucose_level}
          />

          <label>BMI </label>
          <input
              type="number"
              id="bmi"
              name="bmi"
              required
              onChange={(e) => setBmi(e.target.value)}
              value={bmi}
          />
          <input type="submit" value="Submit"></input>       
                   
        </form>
      </div>
    </div>
    
    
  )
}
export default Predict;