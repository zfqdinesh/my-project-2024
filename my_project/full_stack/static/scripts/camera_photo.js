const cameraVideo = document.getElementById('cameraVideo');
const snap = document.getElementById('snap');
const canvas = document.getElementById('canvas');
const context = canvas.getContext('2d');

navigator.mediaDevices.getUserMedia({ video: true })
    .then(stream => {
        cameraVideo.srcObject = stream;
    })
    .catch(err => {
        console.error("Error accessing the camera: ", err);
    });

snap.addEventListener('click', () => {
    context.drawImage(cameraVideo, 0, 0, 640, 480);
});
