// Task 1: Speech to Text
function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.onstart = function() {
        document.getElementById('result').innerText = "Listening...";
    };
    recognition.onspeechend = function() {
        recognition.stop();
        document.getElementById('result').innerText = "Stopped listening.";
    };
    recognition.onresult = function(event) {
        const transcript = event.results[0][0].transcript;
        document.getElementById('result').innerText = "You said: " + transcript;
    };
    recognition.onerror = function(event) {
        document.getElementById('result').innerText = "Error: " + event.error;
    };
    recognition.start();
}
