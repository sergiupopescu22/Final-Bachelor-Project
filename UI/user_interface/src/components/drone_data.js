import React, { useState, useEffect } from "react";

export default function GetDroneData() {
  const [data, setData] = useState([]);

  useEffect(() => {
    fetchData();
  }, []);

  async function fetchData() {
    const response = await fetch("http://192.168.88.15:8000/info_state");
    const data = await response.json();
    setData(data);
  }

  return (
    <div>
        <div>
          <p>Arm State: {data.arm_state}</p>
          <p>Flight Mode: {data.flight_mode}</p>
          <p>Altitude: {data.altitude}</p>
          <p>Latitude: {data.latitude}</p>
          <p>Longitude: {data.longitude}</p>
        </div>
    </div>
  );
}