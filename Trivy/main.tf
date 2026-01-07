provider "aws" {
  region = "us-east-1"
}

resource "aws_s3_bucket" "insecure_bucket" {
  bucket = "my-very-vulnerable-data-bucket"
}

# VULNERABILITY: Public access is not blocked
resource "aws_s3_bucket_public_access_block" "bad_practice" {
  bucket = aws_s3_bucket.insecure_bucket.id

  block_public_acls       = false
  block_public_policy     = false
  ignore_public_acls      = false
  restrict_public_buckets = false
}