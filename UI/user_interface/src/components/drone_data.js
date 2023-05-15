import React, { useState, useEffect } from "react";
import { DRONE_URL } from "./global_var";
let firstRender = true;

export default function GetDroneData(props) {
  const [data, setData] = useState([]);

  useEffect(() => {
    const interval = setInterval(() => {
      fetchData();
    }, 3000); 
    return () => clearInterval(interval);
  }, []);

  async function fetchData() {
    try {
      // console.log(DRONE_URL)
      // console.log({DRONE_URL})
      const response = await fetch(DRONE_URL+'/info_state/');
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
        <div className="drone_info">
          <table>
          <thead>
            <tr>
              <th>Drone Info</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {/* <tr>
              <td>Arm State:</td>
              <td>{data.arm_state}</td>
            </tr>
            <tr>
              <td>Flight Mode:</td>
              <td>{data.flight_mode}</td>
            </tr> */}
            <p></p>
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