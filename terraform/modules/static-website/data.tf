# https://barneyparker.com/posts/uploading-file-trees-to-s3-with-terraform/
locals {
  mime_types = {
    # https://docs.w3cub.com/http/basics_of_http/mime_types/complete_list_of_mime_types.html
    "css"  = "text/css"
    "html" = "text/html"
    "ico"  = "image/vnd.microsoft.icon"
    "js"   = "application/javascript"
    "json" = "application/json"
    "map"  = "application/json"
    "png"  = "image/png"
    "svg"  = "image/svg+xml"
    "txt"  = "text/plain"
    "jpg"  = "image/jpg"
    "pdf"  = "application/pdf"
    "doc"  = "application/msword"
    "gif"  = "image/gif"
    "md"   = "text/markdown"
  }
}
