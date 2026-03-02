# Development Dockerfile for Next.js with hot reload
FROM node:20-alpine

WORKDIR /app

# Copy package files
COPY package.json ./

# Install dependencies
RUN npm install

# Copy source code (will be overridden by volume mount for hot reload)
COPY . .

# Expose port
EXPOSE 8000

# Run in development mode with hot reload
CMD ["npm", "run", "dev", "--", "-p", "8000"]
