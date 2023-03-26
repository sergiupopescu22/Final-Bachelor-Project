import React, { useState, useEffect} from 'react';
import axios from 'axios';

import GetDroneData from './components/drone_data.js';
import Map from './components/map.js';

function App() {

  const [data, setData] = useState('');
  const [loadMap, setLoadMap] = useState(false);
  const [dronePosition, setDronePosition] = useState({ lat: 0, lng: 0 });
  const [center, setCenter] = useState({ lat: 0, lng: 0 });
  const [droneID, setDroneID] = useState("-");
  const [connStatus, setConnStatus] = useState("NO CONNECTION");

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
      <div className="firstRow">
      <h1 className="box">Control Interface</h1>
      <h1 className="box">Drone ID: {droneID}</h1>
      <h1 className="box" style={{ color: {connStatus} == "CONNECTED" ? "red" : "green" }}>Status: {connStatus}</h1>
      </div>
      <div className="buttons_container">
        <button className="button-24" onClick={() => handleClick(1)}>ARM</button>
        <button className="button-24" onClick={() => handleClick(2)}>DISARM</button>
        <br></br>
        <button className="button-24" onClick={() => handleClick(3)}>TAKEOFF Mode</button>
        <button className="button-24" onClick={() => handleClick(4)}>LAND Mode</button>
        <br></br>
        <button className="button-24" onClick={() => handleClick(7)}>MISSION Mode</button>
        <button className="button-24" onClick={() => handleClick(8)}>RETURN Mode</button>    

        <div className="drone_info">
          <GetDroneData 
          setDronePosition={setDronePosition}
          setDroneID={setDroneID}
          setConnStatus={setConnStatus}
          />
        </div>    
      </div>

      {dronePosition.lat != 0 && 
      <Map 
      position={dronePosition} 
      />}
    
    </div>
  );
}

export default App;