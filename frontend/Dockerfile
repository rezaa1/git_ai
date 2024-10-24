FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Copy .env file
COPY .env .

# Start the app
CMD ["npm", "start"]
