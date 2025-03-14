# Database & Storage Documentation

## MongoDB Atlas Configuration

### Connection Details
```python
MONGODB_URL=mongodb+srv://aiinterview:<password>@aiinterview.navvk.mongodb.net/
MONGODB_DB_NAME=ai_interview_db
```

### Collections
1. **Users**
   - User profiles
   - Authentication data
   - Interview history

2. **Interviews**
   - Interview sessions
   - Questions and answers
   - Performance metrics
   - AI analysis results

3. **Resumes**
   - Resume documents
   - Parsed data
   - Skill mappings

4. **Roles**
   - Job roles
   - Required skills
   - Interview templates

## AWS S3 Storage

### Configuration
```python
AWS_ACCESS_KEY_ID=<your-access-key>
AWS_SECRET_ACCESS_KEY=<your-secret-key>
AWS_REGION=ap-south-1
S3_BUCKET=aiinterviewprep
```

### Bucket Structure
```
aiinterviewprep/
├── resumes/
│   └── {user_id}/
│       └── {filename}
├── recordings/
│   └── {interview_id}/
│       ├── audio/
│       └── video/
└── avatars/
    └── responses/
```

## Redis Cloud

### Configuration
```python
REDIS_HOST=redis-xxxxx.c123.us-east-1-1.ec2.cloud.redislabs.com
REDIS_PORT=12345
REDIS_PASSWORD=<your-password>
REDIS_SSL=True
```

### Usage
1. **Rate Limiting**
   - API request tracking
   - User quotas

2. **Caching**
   - Session data
   - Frequently accessed data
   - AI response caching

## Data Models

### User Model
```python
{
    "id": str,
    "email": str,
    "hashed_password": str,
    "full_name": str,
    "created_date": datetime,
    "last_login_date": datetime,
    "is_active": bool
}
```

### Interview Model
```python
{
    "id": str,
    "user_id": str,
    "role_id": str,
    "status": str,
    "start_time": datetime,
    "end_time": datetime,
    "questions": List[Question],
    "answers": List[Answer],
    "voice_metrics": Dict,
    "facial_metrics": Dict,
    "overall_score": float,
    "technical_score": float,
    "communication_score": float
}
```

### Resume Model
```python
{
    "id": str,
    "user_id": str,
    "original_file": str,
    "parsed_data": Dict,
    "confidence_score": float,
    "skill_matches": List[str],
    "status": str
}
```

## Backup & Recovery

### MongoDB Atlas
- Daily automated backups
- Point-in-time recovery
- Manual snapshot option

### S3 Backup
- Versioning enabled
- Cross-region replication
- Lifecycle policies

## Security Measures

1. **Database Security**
   - IP whitelisting
   - Strong passwords
   - Encrypted connections
   - Role-based access

2. **S3 Security**
   - Private bucket policy
   - Encrypted storage
   - Signed URLs for access

3. **Redis Security**
   - SSL/TLS encryption
   - Password authentication
   - Network isolation

## Monitoring

1. **Performance Monitoring**
   - Query performance
   - Connection pooling
   - Cache hit rates

2. **Storage Monitoring**
   - Disk usage
   - Backup status
   - Access patterns

3. **Cost Monitoring**
   - Usage metrics
   - Storage costs
   - API calls 