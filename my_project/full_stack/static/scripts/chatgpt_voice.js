const apiKey = 'your api key'  // Replace with your OpenAI API key
const url = "https://api.openai.com/v1/completions";

let recognition = new (window.SpeechRecognition || window.webkitSpeechRecognition)();
recognition.lang = 'en-US';

document.getElementById('start-record-btn').addEventListener('click', function() {
    recognition.start();
    document.getElementById('status').innerText = "Listening...";
});

recognition.onspeechend = function() {
    recognition.stop();
};

recognition.onresult = function(event) {
    const transcript = event.results[0][0].transcript;
    document.getElementById('question').innerText = transcript;

    fetch(url, {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
            'Authorization': `Bearer ${apiKey}`
        },
        body: JSON.stringify({
            model: "text-davinci-003",  // Model to use, adjust based on your API access
            prompt: transcript,
            max_tokens: 150
        })
    })
    .then(response => response.json())
    .then(data => {
        const response = data.choices[0].text.trim();
        document.getElementById('response').innerText = response;
    })
    .catch(error => {
        console.error('Error:', error);
        document.getElementById('response').innerText = "Error getting response.";
    });
};
