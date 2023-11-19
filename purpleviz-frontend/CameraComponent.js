import React, { useRef, useState, useEffect } from 'react';
import "./CameraComponent.css";
import axios from 'axios';
function CameraComponent() {
  const videoRef = useRef(null);
  const photoRef = useRef(null);

  const [hasPhoto, setHasPhoto] = useState(false);

  useEffect(() => {
    getVideo();
    updateVideoDimensions();
  
    window.addEventListener('resize', updateVideoDimensions);
  
    return () => {
      window.removeEventListener('resize', updateVideoDimensions);
      // ... existing cleanup code ...
    };
  }, []);

  
  
  const updateVideoDimensions = () => {
    const video = videoRef.current;
    if (video) {
      // Adjust padding as needed
      const horizontalPadding = 80;
      const width = window.innerWidth - horizontalPadding; 
      const height = window.innerHeight * 0.75; 
      video.style.width = `${width}px`;
      video.style.height = `${height}px`;
    }
  };

  useEffect(() => {
    getVideo();
  
    // Cleanup function
    return () => {
      const video = videoRef.current;
      if (video && video.srcObject) {
        const tracks = video.srcObject.getTracks();
        tracks.forEach(track => track.stop());
      }
    };
  }, []); // 

  
  const getVideo = () => {
    const video = videoRef.current;
    if (video && video.srcObject) {
      video.srcObject.getTracks().forEach(track => track.stop());
    }
    navigator.mediaDevices
      .getUserMedia({ video: { width: 1920, height: 1080 } })
      .then(stream => {
        const video = videoRef.current;
        if (video) {
          video.srcObject = stream;
          video.play().then(() => {
            // Video playback started successfully
          }).catch(err => {
            console.error('Error attempting to play video:', err);
          });
        }
      })
      .catch(err => {
        console.error(err);
      });
  };



  const takePhoto = () => {
    const width = 414;
    const height = width / (16 / 9);

    let video = videoRef.current;
    let photo = photoRef.current;

    photo.width = width;
    photo.height = height;

    let ctx = photo.getContext('2d');
    ctx.drawImage(video, 0, 0, width, height);
    setHasPhoto(true);
    photo.toBlob(blob => {
      AnalyzePhoto(blob);
    }, 'image/jpeg');
  };

  const AnalyzePhoto = () => {
    if (photoRef.current) {
      const base64Image = photoRef.current.toDataURL('image/jpeg').split(',')[1];
    
      // Axios POST request to Roboflow
      axios({
        method: "POST",
        url: "https://detect.roboflow.com/purpleviz/3",
        params: {
            api_key: "Z1Kv98CZjV9KVqS7kkpf",
            confidence: 1,
        },
        data: base64Image,
        headers: {
            "Content-Type": "application/x-www-form-urlencoded"
        }
      })
      .then(function(response) {
        console.log(response.data);
        // Process the response here
      })
      .catch(function(error) {
        console.error(error.message);
      });
    }
  };
  
  

  const closePhoto = () => {
    let photo = photoRef.current;
    let ctx = photo.getContext('2d');

    ctx.clearRect(0, 0, photo.width, photo.height);
    setHasPhoto(false);
  };

  return (
    <div className="App">
      <div className="camera">
        <video ref={videoRef}></video>
        <button onClick={takePhoto}>SNAP!</button>
      </div>
      <div className={'result ' + (hasPhoto ? 'hasPhoto' : '')}>
        <canvas ref={photoRef}></canvas>
        {hasPhoto && <> <button onClick={AnalyzePhoto}>CONFIRM</button>
            <button onClick={closePhoto}>CLOSE</button></> }
      </div>
    </div>
  );
}

export default CameraComponent;
