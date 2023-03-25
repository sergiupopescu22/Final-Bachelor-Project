import React, { useState } from 'react';
import axios from 'axios';

import GetDroneData from './components/drone_data.js';
import Map from './components/map.js';

function App() {
  const [data, setData] = useState('');

  const [dronePosition, setDronePosition] = useState({ lat: null, lng: null });

  const handleClick = (command) => {
    axios.post('http://192.168.88.15:8000/command/', {type: command} )
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  return (
    <div className="container">
      <h1>Drone Control Interface</h1>
      <div className="buttons_container">
        <button class="button-24" onClick={() => handleClick(1)}>ARM</button>
        <button class="button-24" onClick={() => handleClick(2)}>DISARM</button>
        <br></br>
        <button class="button-24" onClick={() => handleClick(3)}>TAKEOFF Mode</button>
        <button class="button-24" onClick={() => handleClick(4)}>LAND Mode</button>
        <br></br>
        <button class="button-24" onClick={() => handleClick(7)}>MISSION Mode</button>
        <button class="button-24" onClick={() => handleClick(8)}>RETURN Mode</button>    

        <div className="drone_info">
          <GetDroneData setDronePosition={setDronePosition}/>
        </div>    
      </div>
    
      <Map position={dronePosition} setDronePosition={setDronePosition}/>
      
    </div>
  );
}

export default App;