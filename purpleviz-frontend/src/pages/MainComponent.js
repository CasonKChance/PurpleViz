import React, {useState} from 'react';
import axios from 'axios';
import { nanoid } from 'nanoid';

function MainComponent() {
  const [post, setPost] = useState({
    testID: nanoid(),
    toleranceLevel: 'tolerance',
  });
  
  const handleInputChange = (event) => {
    setPost({ ...post, [event.target.name]: event.target.value });
  };
  
  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:8000/api/Test/', post)
      .then(response => {
        console.log(response);
        window.location.href = "http://localhost:3000/camera";
      })
      .catch(error => {
        console.log(error);
      });
  };
  
    return (
      <div style={{display: 'flex', alignItems: 'center', justifyContent: 'center', width: '100%', height: '100vh'}}>
        <div style={{width: '50%', textAlign: 'center'}}>
          <form onSubmit={handleSubmit}>
         
            <input type="text" name="sizeW" placeholder="Size (Width, in)" onChange={handleInputChange} style={{padding: '7.5px', margin: '5px'}}></input><br></br>
            <input type="text" name="sizeL" placeholder="Size (Length, in)" onChange={handleInputChange} style={{padding: '7.5px', margin: '5px'}}></input><br></br>
            <input type="text" name="tolerance" placeholder="Tolerance" onChange={handleInputChange} style={{padding: '7.5px', margin: '5px'}}></input><br></br>
            <button onClick={handleSubmit} style={{width: '15%', marginLeft: 'auto', marginRight: 'auto', marginTop: '15px'}}>Submit</button>
          </form>
  
        </div>
      </div>
    )}
  
  
  export default MainComponent;
  