# My First Node Page

A simple Node.js webpage deployed on Fly.io using Docker.

## Project Structure

```
MyFirstNodePage/
├── app.js           # Main Express server
├── package.json     # Node.js dependencies
├── Dockerfile       # Docker configuration
├── fly.toml         # Fly.io deployment configuration
└── README.md        # This file
```

## How It Works Together

### 1. **app.js** - The Node.js Application
- Runs an Express server listening on port 3000
- Serves a simple HTML page with styling
- Can be extended to add more routes and features

### 2. **package.json** - Dependencies
- Defines the project metadata and npm dependencies
- Currently uses Express.js framework
- `npm ci --only=production` installs only production dependencies (lighter Docker image)

### 3. **Dockerfile** - Docker Configuration
- `FROM node:20-alpine` — Uses a lightweight Node.js image (Alpine Linux)
- `WORKDIR /app` — Sets the working directory inside the container
- `COPY package*.json` — Copies dependency files
- `RUN npm ci --only=production` — Installs dependencies
- `COPY . .` — Copies the entire application
- `EXPOSE 3000` — Opens port 3000 for traffic
- `CMD ["npm", "start"]` — Runs the app when the container starts

### 4. **fly.toml** - Fly.io Configuration
- `app` — Your unique app name on Fly.io
- `primary_region = 'arn'` — Deploys to Aarhus, Denmark region
- `[build]` — Tells Fly.io to use your Dockerfile
- `[http_service]` — Configures HTTP routing (port 3000 internally)
- `[[vm]]` — Resource allocation (1GB RAM, 1 CPU)

## Deployment Flow

1. You run `fly deploy`
2. Fly.io takes your code and Dockerfile
3. Fly.io builds a Docker image from the Dockerfile
4. The image is deployed to a VM in the `arn` region
5. Your app runs inside the container on port 3000
6. Fly.io's proxy handles HTTPS and routes traffic to your app

## Local Testing

**Quick Workflow:**

1. Open Command Prompt in the MyFirstNodePage directory
2. Run the server:
   ```bash
   npm start
   ```
3. Visit `http://localhost:3000` in your browser
4. Make changes to `app.js`, refresh the browser to see updates
5. Stop the server with `Ctrl+C`

**First time setup (if you haven't already):**

```bash
# Install dependencies
npm install
```

This creates `package-lock.json` which locks dependency versions for consistency.

## Deploying to Fly.io

```bash
# Deploy (Fly.io builds and deploys automatically)
fly deploy

# View logs
fly logs
```

## Key Points

- **Lightweight Docker image**: Alpine Linux + Node 20 keeps the image small
- **Security**: HTTPS is enforced by Fly.io (`force_https = true`)
- **Auto-scaling**: Machines start/stop based on traffic (`auto_start_machines = true`)
- **Port mapping**: Internal port 3000 is exposed to the internet via Fly.io
