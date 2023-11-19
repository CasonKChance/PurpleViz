import React, {useState} from 'react';
import axios from 'axios';
import { nanoid } from 'nanoid';

function MainComponent() {
  const [post, setPost] = useState({
    toleranceLevel: '',
    matWidth: '',
    matLength: '',
  });
  
  const handleSubmit = (event) => {
    event.preventDefault();
    axios.post('http://127.0.0.1:8000/api/Test/', post)
      .then(response => {
        console.log(response);
        window.location.href = '/camera'
      })
      .catch(error => {
        console.log(error);
      });
  };

  const handleInputChange = (event) => {
    setPost({ ...post, [event.target.name]: event.target.value });
  };

  return (
    <div style={{ display: 'flex', alignItems: 'center', justifyContent: 'center', width: '100%', height: '100vh' }}>
      <div style={{ width: '50%', textAlign: 'center' }}>
        <form onSubmit={handleSubmit}>
          <input type="text" name="matWidth" placeholder="Size (Width, in)" onChange={handleInputChange} style={{ padding: '7.5px', margin: '5px' }} /><br />
          <input type="text" name="matLength" placeholder="Size (Length, in)" onChange={handleInputChange} style={{ padding: '7.5px', margin: '5px' }} /><br />
          <input type="text" name="toleranceLevel" placeholder="Tolerance" onChange={handleInputChange} style={{ padding: '7.5px', margin: '5px' }} /><br />
          <button type="submit" style={{ width: '15%', marginLeft: 'auto', marginRight: 'auto', marginTop: '15px' }}>Submit</button>
        </form>
      </div>
    </div>
  );
}
  
  
  export default MainComponent;
  