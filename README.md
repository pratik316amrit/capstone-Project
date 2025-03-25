# AZURE AI-Powered Dynamic Ad System

## Overview
This project is an AI-powered advertisement system that dynamically collects user data, stores it in Azure Blob Storage, and retrieves the data to generate targeted ads using Azure's LLMs and DALL·E. The system then displays ads at intervals using Flask and JavaScript.

## Features
- **Dynamic Data Collection:** Gathers user interaction data.
- **Azure Blob Storage Integration:** Stores and retrieves user data securely.
- **Targeted Ad Generation:** Uses Azure OpenAI's LLMs and DALL·E to generate customized advertisements.
- **Flask Backend:** Manages data flow, AI processing, and ad serving.
- **JavaScript Frontend:** Displays ads dynamically at set intervals.
- **Browser Extension:** Collects user data for more accurate ad targeting.

## Tech Stack
- **Backend:** Flask, Azure Blob Storage, Azure OpenAI API (LLM & DALL·E)
- **Frontend:** JavaScript, HTML, CSS
- **Database:** Azure Blob Storage
- **Hosting:** Azure App Services / Any Cloud Provider
- **Extension:** Chrome/Firefox Extension for data collection

## Installation
### Prerequisites
- Python 3.x
- Azure account with OpenAI & Blob Storage enabled
- Flask & necessary Python libraries
- Google Chrome / Mozilla Firefox (for extension installation)

### Steps
1. Install the browser extension (Required for Data Collection):
   - Open Chrome/Firefox and go to `chrome://extensions/` (Chrome) or `about:addons` (Firefox).
   - Enable Developer Mode (Chrome).
   - Click on **Load unpacked** (Chrome) or **Debug Add-ons** (Firefox).
   - Select the `extension` folder from the cloned repository.
   - The extension should now be installed and collecting user data.

2. Clone the repository:
   ```sh
   git clone https://github.com/yourusername/ai-ad-system.git
   cd ai-ad-system
   ```
3. Install backend dependencies:
   ```sh
   pip install -r requirements.txt
   ```
4. Set up Azure Blob Storage and OpenAI API keys in `.env`:
   ```env
   AZURE_STORAGE_ACCOUNT_NAME=your_account_name
   AZURE_STORAGE_ACCOUNT_KEY=your_storage_key
   AZURE_OPENAI_API_KEY=your_openai_api_key
   ```
5. Run the Flask backend:
   ```sh
   python app.py
   ```
6. Navigate to the frontend folder and start the server:
   ```sh
   cd frontend
   npm install
   npm start
   ```
7. Open `http://localhost:3000` in your browser to see ads dynamically displayed.

## Usage
- Users interact with the system, and their data is stored in Azure Blob Storage.
- The backend retrieves user data, processes it with Azure's LLMs & DALL·E, and generates targeted ads.
- The frontend periodically fetches and displays the ads using JavaScript.
- The browser extension enhances user data collection for more precise targeting.

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss your ideas.

## License
This project is licensed under the MIT License.

## Contact
For any inquiries, feel free to reach out:
- **Email:** your-email@example.com
- **GitHub:** [yourusername](https://github.com/yourusername)
