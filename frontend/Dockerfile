FROM node:14 as build

WORKDIR /app

# Copy package.json and package-lock.json (if available)
COPY package*.json ./

# Clear npm cache, remove node_modules, and install dependencies
RUN npm install

# Copy the rest of the frontend code
COPY . .

# Build the React app
RUN npm run build

FROM nginx:alpine

COPY --from=build /app/build /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
