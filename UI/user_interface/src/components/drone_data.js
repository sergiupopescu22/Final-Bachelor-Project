import React, { useState, useEffect } from "react";

export default function GetDroneData(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetchData();
    }, 1000); // fetch data every 5 seconds
    return () => clearInterval(interval);
  }, []);

  async function fetchData() {
    const response = await fetch("http://192.168.88.15:8000/info_state");
    const data = await response.json();
    setData(data);
    // console.log(data.latitude)
    // console.log(data.longitude)
    props.setDronePosition({ lat: data.latitude, lng: data.longitude });
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