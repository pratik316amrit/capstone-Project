// Notify user when the extension is installed
chrome.runtime.onInstalled.addListener(() => {
    chrome.notifications.create({
        type: "basic",
        iconUrl: "icon.png",
        title: "Tracking Disabled",
        message: "Enable tracking in the popup to collect browsing data."
    });
});

// Track user browsing history (ONLY if they have given consent)
chrome.history.onVisited.addListener((historyItem) => {
    chrome.storage.local.get("trackingEnabled", (data) => {
        if (!data.trackingEnabled) return; // Stop tracking if consent is not given

        fetch("http://127.0.0.1:5000/api/track", {
            method: "POST",
            headers: { "Content-Type": "application/json" },
            body: JSON.stringify({ url: historyItem.url })
        })
        .then(response => response.json())
        .then(data => console.log(data));

        

        // Save to local storage
        chrome.storage.local.get({ history: [] }, (storedData) => {
            let history = storedData.history;
            history.push({ url: historyItem.url, time: new Date().toISOString() });

            // Store only the last 100 URLs
            if (history.length > 100) history.shift();

            chrome.storage.local.set({ history });
        });
    });
});

