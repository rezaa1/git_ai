FROM node:14

WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Clear npm cache and install dependencies
RUN npm cache clean --force && npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app
RUN npm run build

# Serve the app using a lightweight server
RUN npm install -g serve

CMD ["serve", "-s", "build", "-l", "3000"]
