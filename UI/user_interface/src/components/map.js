

import { useState, useMemo, useEffect } from "react";
import { GoogleMap, LoadScript, Marker} from "@react-google-maps/api";
import axios from 'axios'

// export default function Map() {
// //   const center = useMemo(() => ({ lat: 45.75, lng: 21.23  }), []);

//   const [markers, setMarkers] = useState([]);
//   const [posts, setPosts] = useState([])

//   const { isLoaded } = useLoadScript({
//     googleMapsApiKey: "AIzaSyDDMP3YyKRuP0NJdERyfK63W9UBjxeEKaw"
//   });


//    const center = {
//     lat: 37.7749,
//     lng: -122.4194
//   };

//   if (!isLoaded) return <div>Loading...</div>;

//   return (
//     <>
//       <GoogleMap
//       zoom={12}
//       center = {center}
//       mapContainerClassName="gmaps-container">
    
//       <></>
//       </GoogleMap>
//     </>
//   );
// }

const containerStyle = {
    width: '400px',
    height: '400px'
  };
  
  const center = {
    lat: -3.745,
    lng: -38.523
  };
  
export default function Map() {

    return (
    <LoadScript
        googleMapsApiKey="AIzaSyDDMP3YyKRuP0NJdERyfK63W9UBjxeEKaw"
    >
        <GoogleMap
        mapContainerClassName="gmaps-container"
        center={center}
        zoom={10}
        >
        <></>
        </GoogleMap>
    </LoadScript>
    )
}