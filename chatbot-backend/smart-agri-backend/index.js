const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');
const axios = require('axios');

const app = express();
const port = 5000;

app.use(cors());
app.use(bodyParser.json());

app.post('/api/ask', async (req, res) => {
  const prompt = req.body.message;
  console.log("🟢 Prompt received:", prompt);

  try {
const response = await axios.post('http://127.0.0.1:11434/api/generate', {
      model: 'tinyllama',
      prompt: prompt,
      stream: false
    });

    const reply = response.data.response;
    console.log("🧠 Model response:", reply);
    res.json({ reply });
  } catch (error) {
    console.error("❌ Error from Ollama API:", error.message);
    res.status(500).json({ error: 'Failed to get response from tinyllama.' });
  }
});

app.listen(port, () => {
  console.log(`✅ Backend running at http://localhost:${port}`);
});