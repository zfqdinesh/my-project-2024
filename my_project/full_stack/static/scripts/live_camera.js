const liveVideo = document.getElementById('liveVideo');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        liveVideo.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing the camera: ", err);
    });
