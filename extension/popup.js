document.addEventListener("DOMContentLoaded", function () {
    let historyList = document.getElementById("historyList");
    let consentButton = document.getElementById("consentButton");
    let statusText = document.getElementById("status");
    let disableConsent = document.getElementById("disableConsent");

    if (!historyList || !consentButton || !statusText) {
        console.error("Required elements not found in the DOM.");
        return;
    }

    // Check if user has already given consent
    chrome.storage.local.get("trackingEnabled", (data) => {
        if (data?.trackingEnabled) {
            statusText.textContent = "Tracking is enabled.";
            consentButton.style.display = "none"; // Hide button if already enabled

            // Load browsing history only if tracking is enabled
            chrome.storage.local.get("history", (historyData) => {
                let history = historyData.history || []; // Ensure it's an array
                historyList.innerHTML = history
                    .slice(-10)
                    .map((item) => `<li>${item.url}</li>`)
                    .join("");
            });
        }
    });

    // Handle user consent
    consentButton.addEventListener("click", function () {
        chrome.storage.local.set({ trackingEnabled: true }, () => {
            statusText.textContent = "Tracking is enabled.";
            consentButton.style.display = "none";
            disableConsent.style.display = "block";

            // Ensure notifications permission exists
            chrome.notifications.create({
                type: "basic",
                iconUrl: "icon.png",
                title: "Tracking Enabled",
                message: "Your browsing activity will now be tracked."
            });
        });
    });

    // Disable user consent
    disableConsent.addEventListener("click", function () {
        chrome.storage.local.set({ trackingEnabled: false }, () => {
            statusText.textContent = "Tracking is disabled.";
            disableConsent.style.display = "none";
            consentButton.style.display = "block";

            chrome.storage.local.remove("history", () => {
                console.log("Browsing history cleared.");
                document.getElementById("historyList").innerHTML = ""; // Clear UI
                chrome.notifications.create({
                    type: "basic",
                    iconUrl: "icon.png",
                    title: "History Cleared",
                    message: "Your tracked browsing history has been deleted."
                });
            });

            // Ensure notifications permission exists
            chrome.notifications.create({
                type: "basic",
                iconUrl: "icon.png",
                title: "Tracking Disabled",
                message: "Your browsing activity will not be tracked."
            });
        });
    });
});
