# Deployment Documentation

## Prerequisites
- Node.js 18+
- Python 3.9+
- MongoDB Atlas account
- AWS account with S3 and Rekognition access
- OpenAI API key
- Redis Cloud account

## Environment Setup

### Backend Environment Variables (.env)
```env
# Server
PORT=8000
HOST=0.0.0.0
SECRET_KEY=your-strong-secret-key

# MongoDB Atlas
MONGODB_URI=mongodb+srv://<username>:<password>@<cluster>.mongodb.net/<dbname>

# Redis Cloud
REDIS_HOST=redis-xxxxx.c123.region-1-1.ec2.cloud.redislabs.com
REDIS_PORT=15370
REDIS_PASSWORD=your-redis-password
REDIS_SSL=true

# AWS
AWS_ACCESS_KEY_ID=your-access-key
AWS_SECRET_ACCESS_KEY=your-secret-key
AWS_REGION=ap-south-1
AWS_BUCKET_NAME=your-bucket-name

# OpenAI
OPENAI_API_KEY=your-openai-key

# CORS
ALLOWED_ORIGINS=["https://yourdomain.com"]
```

### Frontend Environment Variables (.env)
```env
NEXT_PUBLIC_API_URL=https://api.yourdomain.com
NEXT_PUBLIC_WS_URL=wss://api.yourdomain.com
```

## Backend Deployment (Railway)

1. **Create Railway Project**
   ```bash
   railway login
   railway init
   ```

2. **Configure Environment Variables**
   - Add all backend environment variables in Railway dashboard

3. **Deploy Backend**
   ```bash
   railway up
   ```

4. **Configure Domain**
   - Add custom domain in Railway dashboard
   - Update DNS records

## Frontend Deployment (Vercel)

1. **Install Vercel CLI**
   ```bash
   npm i -g vercel
   ```

2. **Configure Project**
   ```bash
   vercel login
   vercel
   ```

3. **Configure Environment Variables**
   - Add frontend environment variables in Vercel dashboard

4. **Deploy Frontend**
   ```bash
   vercel --prod
   ```

## Database Setup

### MongoDB Atlas
1. Create cluster
2. Configure network access
3. Create database user
4. Get connection string
5. Configure collections and indexes

### Redis Cloud
1. Create subscription
2. Create database
3. Configure SSL
4. Get connection details
5. Set up rate limiting

## AWS Configuration

### S3 Setup
1. Create bucket
2. Configure CORS
   ```json
   [
     {
       "AllowedHeaders": ["*"],
       "AllowedMethods": ["GET", "PUT", "POST", "DELETE"],
       "AllowedOrigins": ["https://yourdomain.com"],
       "ExposeHeaders": []
     }
   ]
   ```
3. Configure bucket policy
4. Enable versioning

### IAM Configuration
1. Create IAM user
2. Attach policies:
   - AmazonS3FullAccess
   - AmazonRekognitionFullAccess
3. Generate access keys

## SSL/TLS Configuration

1. **Backend SSL**
   - Managed by Railway
   - Automatic SSL certificate
   - Force HTTPS

2. **Frontend SSL**
   - Managed by Vercel
   - Automatic SSL certificate
   - Force HTTPS

## Monitoring Setup

1. **Application Monitoring**
   - Set up Sentry
   - Configure error tracking
   - Set up performance monitoring

2. **Server Monitoring**
   - Configure Railway metrics
   - Set up alerts

3. **Database Monitoring**
   - MongoDB Atlas monitoring
   - Redis Cloud monitoring
   - Set up alerts

## Backup Strategy

1. **Database Backups**
   - MongoDB Atlas automated backups
   - Daily backup retention
   - Point-in-time recovery

2. **S3 Backups**
   - Enable versioning
   - Configure lifecycle rules
   - Cross-region replication

## Security Measures

1. **API Security**
   - Rate limiting
   - JWT authentication
   - CORS configuration
   - Input validation

2. **Infrastructure Security**
   - SSL/TLS encryption
   - Secure environment variables
   - IAM role restrictions
   - Network security groups

## Scaling Configuration

1. **Backend Scaling**
   - Railway auto-scaling
   - Load balancer configuration
   - Memory/CPU limits

2. **Database Scaling**
   - MongoDB Atlas scaling
   - Redis Cloud scaling
   - Connection pooling

3. **Storage Scaling**
   - S3 bucket lifecycle rules
   - CDN configuration
   - Media optimization

## Maintenance Procedures

1. **Updates and Patches**
   - Regular dependency updates
   - Security patches
   - Version control

2. **Backup Verification**
   - Regular backup testing
   - Restore procedures
   - Data integrity checks

3. **Performance Optimization**
   - Regular performance audits
   - Database optimization
   - Cache management

## Troubleshooting Guide

1. **Common Issues**
   - Connection timeouts
   - Memory issues
   - Rate limit errors
   - Storage quota exceeded

2. **Monitoring Alerts**
   - Error rate spikes
   - High latency
   - Resource exhaustion
   - Authentication failures

3. **Recovery Procedures**
   - Service restart
   - Backup restoration
   - Cache clearing
   - SSL certificate renewal 