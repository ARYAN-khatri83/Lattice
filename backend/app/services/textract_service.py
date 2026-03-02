"""
AWS Textract service for document text extraction
"""
import boto3
from botocore.exceptions import ClientError
from app.config import settings
import logging
from typing import Tuple, Optional

logger = logging.getLogger(__name__)


class TextractService:
    """Service for AWS Textract operations"""
    
    def __init__(self):
        """Initialize Textract client"""
        self.textract_client = boto3.client(
            'textract',
            aws_access_key_id=settings.aws_access_key_id,
            aws_secret_access_key=settings.aws_secret_access_key,
            region_name=settings.aws_region
        )
        self.bucket_name = settings.s3_bucket_name
    
    def extract_text_from_s3(self, s3_key: str) -> Tuple[Optional[str], Optional[float], Optional[str]]:
        """
        Extract text from document in S3 using Textract
        
        Args:
            s3_key: S3 key/path of the document
            
        Returns:
            Tuple of (extracted_text, confidence_score, error_message)
            - extracted_text: Combined text from all LINE blocks
            - confidence_score: Average confidence across all LINE blocks
            - error_message: Error description if extraction failed
        """
        try:
            logger.info(f"Starting Textract extraction for s3://{self.bucket_name}/{s3_key}")
            
            # Call Textract detect_document_text
            response = self.textract_client.detect_document_text(
                Document={
                    'S3Object': {
                        'Bucket': self.bucket_name,
                        'Name': s3_key
                    }
                }
            )
            
            # Extract LINE blocks and compute confidence
            lines = []
            confidences = []
            
            for block in response.get('Blocks', []):
                if block['BlockType'] == 'LINE':
                    # Extract text
                    text = block.get('Text', '').strip()
                    if text:
                        lines.append(text)
                    
                    # Extract confidence
                    confidence = block.get('Confidence')
                    if confidence is not None:
                        confidences.append(confidence)
            
            # Combine lines into single text blob
            extracted_text = '\n'.join(lines)
            
            # Compute average confidence
            avg_confidence = sum(confidences) / len(confidences) if confidences else None
            
            logger.info(
                f"Textract extraction completed: {len(lines)} lines, "
                f"avg confidence: {avg_confidence:.2f}%" if avg_confidence else "N/A"
            )
            
            return extracted_text, avg_confidence, None
            
        except ClientError as e:
            error_code = e.response.get('Error', {}).get('Code', 'Unknown')
            error_msg = f"Textract ClientError ({error_code}): {str(e)}"
            logger.error(error_msg)
            return None, None, error_msg
            
        except Exception as e:
            error_msg = f"Textract extraction failed: {str(e)}"
            logger.error(error_msg)
            return None, None, error_msg


# Global Textract service instance
textract_service = TextractService()
