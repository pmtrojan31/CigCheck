# CigCheck: Computer Vision Powered Cigarette Detection Chatbot

## 🚀 Introduction
CigCheck is a computer vision powered chatbot that detects cigarettes in images and raises awareness about the health risks of smoking. By leveraging computer vision, the bot analyzes uploaded images and provides informative responses based on the detection results.

## 🔧 How It Works
1. **Start the Chatbot** - The chatbot will greet you and provide instructions.
2. **Upload an Image** - Type `UPLOAD IMAGE` and press enter.
3. **Provide the Image Name** - Enter the file name (including extension) after uploading it to the test_images folder in the project directory.
4. **Cigarette Detection** - The bot analyzes the image:
   - If a cigarette is detected, it confirms the presence and provides a brief summary of smoking's health risks.
   - If no cigarette is found, it informs the user accordingly.
5. **Make conversation** - Feel free to speak with the chatbot regarding the cons of smoking or anything in general.
5. **End the Session** - Type `STOP` to exit the chatbot.

## 📂 Installation & Setup
### Prerequisites
- Python 3.x
- Required dependencies from `requirements.txt'
- OpenAI API Key (for chatbot responses) ("gpt-4o-mini" is the gpt model used)
- Roboflow API Key (for cigarette detection model)

### Installation Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/smokeguard.git
   cd smokeguard
   ```
2. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Set up environment variables:
   Create a .env file containing youre OPENAI_API_KEY and ROBOFLOW_API_KEY. An example is shown in .env.example
   
5. Run the chatbot:
   ```sh
   python main.py
   ```

## ⚙️ Technologies Used
- **Python** - Core language for chatbot and image processing
- **OpenAI API** - Powers the chatbot's conversational abilities
- **Roboflow API** - Performs cigarette detection in images

  
🚭 **Say no to smoking! Let’s spread awareness together.**

