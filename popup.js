document.getElementById("analyzeButton").addEventListener("click", function() {
    const topic = document.getElementById("topicInput").value;

    fetch(`http://127.0.0.1:5000/sentiment?topic=${encodeURIComponent(topic)}`)
        .then(response => {
            if (!response.ok) {
                throw new Error("Network response was not ok");
            }
            return response.json();
        })
        .then(data => {
            const resultElement = document.getElementById("result");
            if (resultElement) {
                resultElement.textContent = `Sentiment: ${data.sentiment}`;
            }
        })
        .catch(error => {
            console.error('Error:', error);
            const resultElement = document.getElementById("result");
            if (resultElement) {
                resultElement.textContent = "Failed to analyze sentiment.";
            }
        });
});
