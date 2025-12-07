# Use Nginx to serve static files
FROM nginx:alpine

# Copy build files to nginx html directory
COPY ./templatemo_564_plot_listing /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
