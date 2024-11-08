async function sendMessage() {
  const userInput = document.getElementById("user-input");
  const chatBox = document.getElementById("chat-box");
  const userMessage = userInput.value.trim();

  if (userMessage === "") return;

  // Display user message
  appendMessage(userMessage, "user");

  // Clear input field
  userInput.value = "";

  // Send request to the server
  try {
      const response = await fetch("/size-match", {
          method: "POST",
          headers: {
              "Content-Type": "application/json"
          },
          body: JSON.stringify({ message: userMessage })
      });
      const data = await response.json();

      // Display bot response
      appendMessage(data.response, "bot");
  } catch (error) {
      console.error("Error:", error);
      appendMessage("There was an error processing your request.", "bot");
  }
}

function appendMessage(text, sender) {
  const chatBox = document.getElementById("chat-box");
  const messageDiv = document.createElement("div");
  messageDiv.classList.add("message", sender);
  messageDiv.innerText = text;
  chatBox.appendChild(messageDiv);
  chatBox.scrollTop = chatBox.scrollHeight;
}
