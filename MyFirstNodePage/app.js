const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('.'));

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="en">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Hot People spotted in New York</title>
      <style>
        body {
          font-family: Arial, sans-serif;
          display: flex;
          justify-content: center;
          align-items: center;
          min-height: 100vh;
          margin: 0;
          background: linear-gradient(135deg, #ff6b6b 0%, #ee5a6f 100%);
          padding: 20px;
        }
        .container {
          text-align: center;
          background: white;
          padding: 40px;
          border-radius: 10px;
          box-shadow: 0 10px 25px rgba(0,0,0,0.2);
          max-width: 600px;
        }
        h1 {
          color: #333;
          margin: 0;
          font-size: 2.5em;
        }
        .hearts {
          font-size: 2em;
          margin: 10px 0;
        }
        img {
          max-width: 100%;
          height: auto;
          border-radius: 8px;
          margin-top: 20px;
          box-shadow: 0 5px 15px rgba(0,0,0,0.2);
        }
        p {
          color: #666;
          margin-top: 10px;
          font-size: 1.1em;
        }
      </style>
    </head>
    <body>
      <div class="container">
        <h1>Hot People spotted in New York ❤️</h1>
        <div class="hearts">❤️ ❤️ ❤️</div>
        <img src="HotStuffInNewYork.JPG" alt="Hot Stuff in New York">
        <p>Check out these amazing vibes from NYC!</p>
      </div>
    </body>
    </html>
  `);
});

app.listen(PORT, () => {
  console.log(`Server running on port ${PORT}`);
});
