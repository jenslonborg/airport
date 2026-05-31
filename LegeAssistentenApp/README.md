# Lege Assistenten

A colorful, pixelated game picker app for kids. Choose between indoor and outdoor games!

## Project Structure

```
LegeAssistentenApp/
├── app.js              # Express server with all routes and HTML/CSS
├── package.json        # Project dependencies and scripts
├── README.md           # This file
├── .gitignore          # Ignores node_modules folder
└── Images/
    ├── IndeLege.png    # Indoor games button image
    └── UdeLege.png     # Outdoor games button image
```

## Features

- **Landing Page**: Two large image buttons to choose between indoor and outdoor games
- **Game Lists**: Separate pages showing available games for each category
- **Pixelated Design**: Retro pixel art style with pastel colors and rounded edges
- **Mobile Responsive**: Optimized for phone and tablet screens
- **Simple Architecture**: Single-file Express server with inline HTML/CSS

## Prerequisites

- Node.js 18 or higher
- npm (comes with Node.js)

## Installation

1. Navigate to the project folder:
   ```bash
   cd LegeAssistentenApp
   ```

2. Install dependencies:
   ```bash
   npm install
   ```

## Running the App Locally

Start the server:
```bash
npm start
```

The app will start on `http://localhost:3000`. Open this URL in your browser to see the app.

## How to Add or Edit Games

Edit the `indoorGames` and `outdoorGames` arrays in `app.js`:

```javascript
const indoorGames = [
  'Lego',
  'Brætspil',
  // ... add more games here
];

const outdoorGames = [
  'Gemmeleg',
  'Fangeleg',
  // ... add more games here
];
```

After making changes, restart the server (stop with Ctrl+C, then run `npm start` again).

## Customization

### Colors
Edit the color values in the `baseStyles` constant in `app.js`:
- `#e8d5f5` - Background lavender
- `#ffb3c6` - Pastel pink (accent)
- `#b3f0d4` - Pastel mint (accent)

### Font
The app uses "Press Start 2P" from Google Fonts for the pixelated look. Change the `font-family` in `baseStyles` to use a different font.

### Images
Replace the PNG files in the `Images/` folder with your own button images. Keep them named `IndeLege.png` and `UdeLege.png`.

## Deployment to Fly.io

This app is already configured for Fly.io deployment. The `fly.toml` file contains all the necessary configuration.

### Prerequisites
- Install [Flyctl](https://fly.io/docs/getting-started/installing-flyctl/)
- Create a Fly.io account (free tier available)
- Authenticate with Fly.io: `flyctl auth login`

### Deploy Steps

1. **First time deployment** (if not already set up):
   ```bash
   flyctl launch
   ```
   This will create the app on Fly.io using settings from `fly.toml`.

2. **Deploy your changes**:
   ```bash
   flyctl deploy
   ```
   This builds the Docker image and deploys it to Fly.io.

3. **View your app**:
   The app will be available at `https://lege-assistenten.fly.dev` (or your configured domain).

4. **Monitor logs**:
   ```bash
   flyctl logs
   ```

5. **SSH into the app** (for debugging):
   ```bash
   flyctl ssh console
   ```

### How It Works

- **Dockerfile**: Builds a lightweight Node.js Alpine image
- **fly.toml**: Configures the app to run in the `arn` region (Aarhus, Denmark) with auto-start/stop enabled
- **Port 3000**: The app runs on port 3000 inside the container, exposed via HTTPS to the internet

Your app will auto-scale to zero machines when idle (cost-saving) and automatically start when accessed.
