FROM mcr.microsoft.com/playwright:v1.56.1-noble
WORKDIR /tests
COPY ./package.json package.json
RUN npm install
CMD echo playwright installed