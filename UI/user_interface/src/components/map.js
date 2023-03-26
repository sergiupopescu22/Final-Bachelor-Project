import { useState, useMemo, useEffect } from "react";
import { GoogleMap, LoadScript, Marker} from "@react-google-maps/api";
  
export default function Map(props) {

    const center_var = useMemo(()=>(props.position),[]);

    const [loadMarker, setLoadMarker] = useState(false);

    useEffect(() => {
        const timer = setTimeout(() => {
        setLoadMarker(true);
        }, 1000); // wait for 1 second

        return () => clearTimeout(timer);
    }, []);
    
    return (
    <LoadScript
        googleMapsApiKey="AIzaSyDDMP3YyKRuP0NJdERyfK63W9UBjxeEKaw"
    >
        <GoogleMap
        mapContainerClassName="gmaps-container"
        center={center_var}
        zoom={17}
        >
         {loadMarker && <Marker position_drona={props.position} position={props.position}/>}
         
         
        </GoogleMap>

    </LoadScript>
    )
}