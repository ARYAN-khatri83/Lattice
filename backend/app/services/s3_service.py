"""
S3 service for handling file uploads and downloads
"""
import boto3
from botocore.exceptions import ClientError
from app.config import settings
import logging
from typing import Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class S3Service:
    """Service for S3 operations"""
    
    def __init__(self):
        """Initialize S3 client"""
        self.s3_client = boto3.client(
            's3',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )
        self.bucket_name = settings.s3_bucket_name
    
    def upload_file(
        self, 
        file_content: bytes, 
        file_name: str, 
        patient_id: str,
        content_type: str = "application/pdf"
    ) -> Optional[str]:
        """
        Upload file to S3
        
        Args:
            file_content: File content as bytes
            file_name: Original file name
            patient_id: Patient ID for organizing files
            content_type: MIME type of file
            
        Returns:
            S3 key if successful, None otherwise
        """
        try:
            # Generate S3 key with organized structure
            timestamp = datetime.utcnow().strftime("%Y%m%d_%H%M%S")
            s3_key = f"patients/{patient_id}/documents/{timestamp}_{file_name}"
            
            # Upload to S3
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=file_content,
                ContentType=content_type,
                Metadata={
                    'patient_id': str(patient_id),
                    'original_filename': file_name
                }
            )
            
            logger.info(f"Successfully uploaded file to S3: {s3_key}")
            return s3_key
            
        except ClientError as e:
            logger.error(f"Failed to upload file to S3: {str(e)}")
            return None
    
    def download_file(self, s3_key: str) -> Optional[bytes]:
        """
        Download file from S3
        
        Args:
            s3_key: S3 key/path of the file
            
        Returns:
            File content as bytes if successful, None otherwise
        """
        try:
            logger.info(f"Downloading file from S3: {s3_key}")
            response = self.s3_client.get_object(
                Bucket=self.bucket_name,
                Key=s3_key
            )
            file_content = response['Body'].read()
            logger.info(f"Successfully downloaded file: {len(file_content)} bytes")
            return file_content
            
        except ClientError as e:
            logger.error(f"Failed to download file from S3: {str(e)}")
            return None
    
    def get_file_url(self, s3_key: str, expiration: int = 3600) -> Optional[str]:
        """
        Generate presigned URL for file access
        
        Args:
            s3_key: S3 key/path of the file
            expiration: URL expiration time in seconds (default 1 hour)
            
        Returns:
            Presigned URL if successful, None otherwise
        """
        try:
            url = self.s3_client.generate_presigned_url(
                'get_object',
                Params={'Bucket': self.bucket_name, 'Key': s3_key},
                ExpiresIn=expiration
            )
            return url
        except ClientError as e:
            logger.error(f"Failed to generate presigned URL: {str(e)}")
            return None


# Global S3 service instance
s3_service = S3Service()
