document.getElementById('searchButton').addEventListener('click', function() {
    const query = document.getElementById('searchQuery').value;
    const resultsDiv = document.getElementById('results');
    resultsDiv.innerHTML = "Searching for: " + query;

    if (query) {
        const url = `https://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=${encodeURIComponent(query)}&format=json&origin=*`;

        fetch(url)
            .then(response => response.json())
            .then(data => {
                resultsDiv.innerHTML = ""; // Clear previous results

                if (data.query.search.length > 0) {
                    data.query.search.forEach(item => {
                        const result = document.createElement('div');
                        result.innerHTML = `<h3>${item.title}</h3><p>${item.snippet}</p><a href="https://en.wikipedia.org/?curid=${item.pageid}" target="_blank">Read more</a>`;
                        resultsDiv.appendChild(result);
                    });
                } else {
                    resultsDiv.innerHTML = "No results found!";
                }
            })
            .catch(err => {
                resultsDiv.innerHTML = "Error fetching results!";
                console.error("Error: ", err);
            });
    } else {
        resultsDiv.innerHTML = "Please enter a search query!";
    }
});
