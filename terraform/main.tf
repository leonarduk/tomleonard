module "check_tomleonard_co_uk" {
  source = "./modules/web_site_checker"

  function_name        = "test_tomleonard_co_uk"
  function_description = "checks tomleonard.co.uk"
  function_source      = "../python/lambda/check_website"

  expected_text = "Some poems, letters, a web journal 2009-2014, and a page with books for sale can be reached via menu to left."
  tags          = "tomleonard"
  website_url   = "http://tomleonard.co.uk"
}

module "tom_leonard_site" {
  source = "./modules/static-website"

  tag_name         = "tomleonard"
  domain_name      = "www.tomleonard.co.uk"
  upload_directory = "../s3/"
}

