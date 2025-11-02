# Production Docker Setup (NeuraLearn)

This file contains production Docker configuration for the project.

## Files created
- backend/Dockerfile.prod
- ml_service/Dockerfile.prod
- frontend/Dockerfile.prod
- nginx/default.conf
- docker-compose.prod.yml
- .env.example

## Quick start (after editing .env)
1. Copy .env.example to .env and fill real secrets (DB passwords, JWT_SECRET, DOMAIN).
2. Ensure your DNS for DOMAIN points to your server IP.
3. Build and start production stack:
   docker compose -f docker-compose.prod.yml up -d --build

## Obtain SSL certs with certbot container
1. Stop nginx temporarily if it's running locally.
2. Run certbot to obtain certificates (replace YOUR_DOMAIN):
   docker compose -f docker-compose.prod.yml run --rm certbot certonly --webroot --webroot-path=/var/www/html -d YOUR_DOMAIN -d www.YOUR_DOMAIN
3. After successful issuance, certs will be stored in the certs volume and nginx will serve HTTPS.
4. (Optional) set up a cron or systemd timer to renew certs:
   docker compose -f docker-compose.prod.yml run --rm certbot renew --deploy-hook \"docker exec neuralearn_nginx nginx -s reload\"

## Notes
- Update nginx/default.conf server_name and ssl_certificate paths to match your domain.
- Use a secrets manager (Vault / cloud provider secrets) for production secrets if possible.
- For more secure production images, consider adding non-root users and multi-stage minification.
