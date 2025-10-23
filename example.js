const { OpenAI } = require("openai");

// Initialize the Poe client using OpenAI SDK
const client = new OpenAI({
    apiKey: process.env.POE_API_KEY || "YOUR_POE_API_KEY",
    baseURL: "https://api.poe.com/v1",
});

async function generateVideo() {
    try {
        const chat = await client.chat.completions.create({
            model: "Sora2-South-Park",
            messages: [{ role: "user", content: "Hello world" }],
        });

        console.log(chat.choices[0].message.content);
    } catch (error) {
        console.error("Error generating video:", error.message);
    }
}

// Run the example
generateVideo();
