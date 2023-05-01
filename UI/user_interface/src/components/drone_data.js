import React, { useState, useEffect } from "react";
import { DRONE_URL } from "./globals";
let firstRender = true;

export default function GetDroneData(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetchData();
    }, 3000); 
    return () => clearInterval(interval);
  }, []);

  // http://192.168.88.15:8000/info_state
  // proxy51.rt3.io:31682
  async function fetchData() {
    try {
      const response = await fetch(DRONE_URL);
      const data = await response.json();
      setData(data);
      props.setDronePosition({ lat: data.latitude, lng: data.longitude });
      props.setDroneID(data.drone_id)
      props.setConnStatus("CONNECTED")
    } catch (error) {
      console.error("Error fetching data:", error);
      props.setConnStatus("NO CONNECTION")
    }
  }

  return (
        <div>
          <table>
          <thead>
            <tr>
              <th>Drone Info</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            <tr>
              <td>Arm State:</td>
              <td>{data.arm_state}</td>
            </tr>
            <tr>
              <td>Flight Mode:</td>
              <td>{data.flight_mode}</td>
            </tr>
            <tr>
              <td>Altitude</td>
              <td>{data.altitude}</td>
            </tr>
            <tr>
              <td>Relative Altitude:</td>
              <td>{data.relative_altitude}</td>
            </tr>
            <tr>
              <td>Latitude:</td>
              <td>{data.latitude}</td>
            </tr>
            <tr>
              <td>Longitude</td>
              <td>{data.longitude}</td>
            </tr>
          </tbody>
          </table>
</div>
    
  );
}