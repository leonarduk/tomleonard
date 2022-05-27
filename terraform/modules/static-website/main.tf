# https://medium.com/@dblencowe/hosting-a-static-website-on-s3-using-terraform-0-12-aa5ffe4103e
# https://medium.com/@venkat_teja_ravi/s3-deployment-using-terraform-15a3a3a43d5d
# Create a bucket
resource "aws_s3_bucket" "bucket" {
  bucket = var.domain_name
  acl    = "public-read"   # or can be "public-read" or "private"

  website {
    index_document = "index.html"
    error_document = "email-page.html"
  }

  tags = {
    Name        = var.tag_name
    Environment = var.tag_env
  }
  policy = data.aws_iam_policy_document.website_policy.json
}

resource "aws_s3_bucket_object" "dist" {
  for_each = fileset(var.upload_directory, "**/*.*")
  bucket = aws_s3_bucket.bucket.id
  key    = each.value
  source = "${var.upload_directory}/${each.value}"
  etag         = filemd5("${var.upload_directory}/${each.key}")
  content_type = lookup(tomap(local.mime_types), element(split(".", each.key), length(split(".", each.key)) - 1))
}

data "aws_iam_policy_document" "website_policy" {
  statement {
    sid = "ReadOnly"

    actions = [
      "s3:GetObject",
      "s3:GetObjectVersion"
    ]
    principals {
      identifiers = ["*"]
      type = "AWS"
    }
    resources = [
      "arn:aws:s3:::${var.domain_name}/*"
    ]
  }
}