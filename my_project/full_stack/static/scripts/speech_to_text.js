function startListening() {
    const recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
    recognition.lang = 'en-US';
    recognition.onstart = () => {
        document.getElementById('result').innerText = "Listening...";
    };
    recognition.onspeechend = () => {
        recognition.stop();
    };
    recognition.onresult = (event) => {
        const transcript = event.results[0][0].transcript;
        document.getElementById('result').innerText = "You said: " + transcript;
    };
    recognition.onerror = (event) => {
        document.getElementById('result').innerText = "Error: " + event.error;
    };
    recognition.start();
}
