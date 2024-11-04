let mediaRecorder;
let recordedChunks = [];

const recordVideo = document.getElementById('recordVideo');
const startButton = document.getElementById('start');
const stopButton = document.getElementById('stop');
const playbackVideo = document.getElementById('playback');

navigator.mediaDevices.getUserMedia({ video: true, audio: true })
    .then(stream => {
        recordVideo.srcObject = stream;
        mediaRecorder = new MediaRecorder(stream);
        mediaRecorder.ondataavailable = (event) => {
            recordedChunks.push(event.data);
        };
        mediaRecorder.onstop = () => {
            const blob = new Blob(recordedChunks, { type: 'video/mp4' });
            playbackVideo.src = URL.createObjectURL(blob);
            playbackVideo.controls = true;
        };
    })
    .catch(err => {
        console.error("Error accessing the camera: ", err);
    });

startButton.addEventListener('click', () => {
    recordedChunks = [];
    mediaRecorder.start();
});

stopButton.addEventListener('click', () => {
    mediaRecorder.stop();
});
