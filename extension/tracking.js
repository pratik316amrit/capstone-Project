document.addEventListener("DOMContentLoaded", () => {
    chrome.storage.local.get({ history: [] }, (data) => {
        const historyList = document.getElementById("history-list");
        historyList.innerHTML = ""; // Clear old entries

        data.history.forEach(entry => {
            let listItem = document.createElement("li");
            listItem.textContent = `${entry.url} - ${new Date(entry.time).toLocaleString()}`;
            historyList.appendChild(listItem);
        });
    });
});
