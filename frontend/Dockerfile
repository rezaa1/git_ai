FROM node:14

WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Clear npm cache, remove node_modules, and install dependencies
RUN npm cache clean --force && \
    rm -rf node_modules && \
    npm install

# Copy the rest of the frontend code
COPY . .

# Rebuild node-sass
RUN npm rebuild node-sass

# Build the React app
RUN npm run build

# Serve the app using a lightweight server
RUN npm install -g serve

CMD ["serve", "-s", "build", "-l", "3000"]
