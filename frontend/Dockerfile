FROM node:14

WORKDIR /app

COPY package*.json ./
RUN npm install

COPY . .

# Set to development mode
ENV NODE_ENV=development

# Start the app in development mode
CMD ["npm", "start"]
