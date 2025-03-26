function injectAd() {
    let container = document.querySelector("body");
    console.log(container);

    if (!container) {
        console.error("Error: .search-results container not found!");
        return;
    }

    // Check if the ad container already exists
    let adContainer = document.getElementById("custom-ad");
    if (!adContainer) {
        adContainer = document.createElement("div");
        adContainer.id = "custom-ad";
        adContainer.innerHTML = "This is a fixed bottom banner ad."; // Add content

        // Apply styles directly via JavaScript
        Object.assign(adContainer.style, {
            position: "fixed",
            height: "400px",
            bottom: "0",
            right: "0",
            width: "50%",
            background: "rgba(0, 0, 0, 0.8)",
            color: "white",
            textAlign: "center",
            padding: "15px",
            boxShadow: "0 -2px 10px rgba(0, 0, 0, 0.5)",
            zIndex: "9999",
        });

        // Append it to the body
        document.body.appendChild(adContainer);
    }

    
    // Fetch ad content from API
    fetch("http://127.0.0.1:5000/api/ad", {
        method: "GET",
        headers: { "Content-Type": "application/json" },
    })
    .then(response => response.json())
    .then(data => {
        // <p class="information">" ${data.ad_text} "</p>
        // <img src="data:image/png;base64,${data.image_base64}" alt="Ad Image"> alt="Omar Dsoky"></img>
        
        console.log(data.ad_text)
        adContainer.innerHTML = `
            <div id="container">	
	
                <!-- Start	Product details -->
                    <div class="product-details">
                        
                        <!-- 	Product Name -->
                    
                <!-- 		<span class="hint new">New</span> -->
                <!-- 		<span class="hint free-shipping">Free Shipping</span> -->
                <!-- 		the Product rating -->
                    
                        
                    
                <!-- The most important information about the product -->
                        <p class="information">" ${data.ad_text} "</p>
                
                        
                        
                <!-- 		Control -->
                <div class="control">
                    
            
                </div>
                            
                </div>
                    
                <!-- 	End	Product details   -->
                    
                    
                    
                <!-- 	Start product image & Information -->
                    
                <div class="product-image">
                    
                    <img src="data:image/png;base64,${data.image_base64}" alt="Ad Image"> alt="Omar Dsoky"></img>
                    
                <!-- 	product Information-->
                
                </div>
                <!--  End product image  -->
                
                
                </div>
        
        `
    })
    .catch(error => console.error("Error fetching ad data:", error));
}

// Run immediately on page load
injectAd();

// Fetch and inject the ad every 2 minutes
setInterval(injectAd, 120000);
