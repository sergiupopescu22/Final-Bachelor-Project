import React, { useState } from 'react';
import axios from 'axios';

import GetDroneData from './components/drone_data.js';
import Map from './components/map.js';
import { DRONE_URL } from './components/global_var.js';

function App() {
  const [data, setData] = useState('');
  const [dronePosition, setDronePosition] = useState({ lat: 0, lng: 0 });
  const [droneID, setDroneID] = useState("-");
  const [connStatus, setConnStatus] = useState("NO CONNECTION");
  const [visibleForm, setVisibleForm] = useState(false);

  const handleClick = (command) => {
    axios.post(DRONE_URL+"/command/", {type: command} )
      .then(response => {
        setData(response.data);
      })
      .catch(error => {
        console.error(error);
      });
  };

  const makeVisible = () => {
    setVisibleForm(!visibleForm);
  }

  return (
    <div className="container">
        <div>
        <h1 className="box" style={{ color: connStatus === "NO CONNECTION" ? 'red' : 'green' }}>Status: {connStatus}</h1>

        <div className="contorl-panel">
          <h1 className="box">Commands</h1>
          <button className="button-24" onClick={() => handleClick(1)}>ARM</button>
          <button className="button-24" onClick={() => handleClick(2)}>DISARM</button>
          <br></br>
          <button className="button-24" onClick={() => handleClick(3)}>TAKEOFF Mode</button>
          <button className="button-24" onClick={() => handleClick(4)}>LAND Mode</button>
          <br></br>
          <button className="button-24" onClick={() => { makeVisible();}}>MISSION Mode</button>
          <button className="button-24" onClick={() => handleClick(8)}>RETURN Mode</button>    
        </div>

        <GetDroneData 
        setDronePosition={setDronePosition}
        setDroneID={setDroneID}
        setConnStatus={setConnStatus}
        />
        </div>
        {dronePosition.lat !== 0 && connStatus === "CONNECTED" && 
        <Map position={dronePosition} visibleForm={visibleForm}/>}


    </div>
  );
}

export default App;