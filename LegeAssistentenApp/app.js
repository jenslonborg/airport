const express = require('express');
const app = express();
const PORT = process.env.PORT || 3000;

app.use(express.static('.'));

const indoorGames = [
  'Lego',
  'Brætspil',
  'Kortspil',
  'Tegn og gæt',
  'Puslespil',
  'Simon siger',
  'Skjul inde',
  'Dans'
];

const outdoorGames = [
  'Gemmeleg',
  'Fangeleg',
  'Fodbold',
  'Spring tau',
  'Paradis',
  'Cykling',
  'Vandkamp',
  'Rulleskøjter'
];

const baseStyles = `
  @import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

  * {
    margin: 0;
    padding: 0;
    box-sizing: border-box;
  }

  body {
    background: linear-gradient(135deg, #e8d5f5 0%, #f5d5e8 100%);
    font-family: 'Press Start 2P', cursive;
    min-height: 100vh;
    display: flex;
    justify-content: center;
    align-items: center;
    padding: 20px;
  }

  .container {
    background: white;
    border-radius: 20px;
    padding: 30px;
    max-width: 420px;
    width: 100%;
    box-shadow: 0 8px 16px rgba(0, 0, 0, 0.1);
  }

  h1 {
    text-align: center;
    font-size: 18px;
    margin-bottom: 30px;
    color: #333;
    text-shadow: 2px 2px 0px #ffb3c6;
  }

  .button-container {
    display: flex;
    flex-direction: column;
    gap: 20px;
  }

  .image-button {
    position: relative;
    border: none;
    border-radius: 16px;
    overflow: hidden;
    cursor: pointer;
    transition: transform 0.2s ease, box-shadow 0.2s ease;
    padding: 0;
    width: 100%;
    height: auto;
    max-height: 300px;
  }

  .image-button:hover {
    transform: scale(1.05);
    box-shadow: 0 4px 12px rgba(255, 179, 198, 0.4);
  }

  .image-button:active {
    transform: scale(0.98);
  }

  .image-button img {
    width: 100%;
    height: 100%;
    display: block;
    border-radius: 16px;
    image-rendering: pixelated;
  }

  .games-list {
    list-style: none;
  }

  .games-list li {
    background: linear-gradient(135deg, #ffb3c6 0%, #ffc6d9 100%);
    padding: 15px 20px;
    margin-bottom: 10px;
    border-radius: 12px;
    font-size: 12px;
    color: #333;
    text-align: center;
    border: 3px solid #ffffff;
    box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
  }

  .games-list li:nth-child(odd) {
    background: linear-gradient(135deg, #b3f0d4 0%, #b3f0d4 100%);
  }

  .back-button {
    display: inline-block;
    margin-bottom: 20px;
    padding: 10px 20px;
    background: linear-gradient(135deg, #ffb3c6 0%, #ffc6d9 100%);
    color: #333;
    text-decoration: none;
    border-radius: 12px;
    font-size: 10px;
    border: 2px solid #333;
    cursor: pointer;
    transition: transform 0.2s ease;
  }

  .back-button:hover {
    transform: scale(1.05);
  }

  .back-button:active {
    transform: scale(0.95);
  }
`;

app.get('/', (req, res) => {
  res.send(`
    <!DOCTYPE html>
    <html lang="da">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Lege Assistenten</title>
      <style>${baseStyles}</style>
    </head>
    <body>
      <div class="container">
        <h1>Lege Assistenten</h1>
        <div class="button-container">
          <button class="image-button" onclick="window.location.href='/indelege'">
            <img src="/Images/IndeLege.png" alt="Indendørs Lege" />
          </button>
          <button class="image-button" onclick="window.location.href='/udelege'">
            <img src="/Images/UdeLege.png" alt="Udendørs Lege" />
          </button>
        </div>
      </div>
    </body>
    </html>
  `);
});

app.get('/indelege', (req, res) => {
  const gamesList = indoorGames.map(game => `<li>${game}</li>`).join('');

  res.send(`
    <!DOCTYPE html>
    <html lang="da">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Indendørs Lege</title>
      <style>${baseStyles}</style>
    </head>
    <body>
      <div class="container">
        <a href="/" class="back-button">← Tilbage</a>
        <h1>Indendørs Lege</h1>
        <ul class="games-list">
          ${gamesList}
        </ul>
      </div>
    </body>
    </html>
  `);
});

app.get('/udelege', (req, res) => {
  const gamesList = outdoorGames.map(game => `<li>${game}</li>`).join('');

  res.send(`
    <!DOCTYPE html>
    <html lang="da">
    <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Udendørs Lege</title>
      <style>${baseStyles}</style>
    </head>
    <body>
      <div class="container">
        <a href="/" class="back-button">← Tilbage</a>
        <h1>Udendørs Lege</h1>
        <ul class="games-list">
          ${gamesList}
        </ul>
      </div>
    </body>
    </html>
  `);
});

app.listen(PORT, () => {
  console.log(`Server running on http://localhost:${PORT}`);
});
