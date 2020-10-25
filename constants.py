checkout = 'checkout'
git = 'git'
fetch = 'fetch'
master = 'master'
origin = 'origin'
staging = 'staging'
production = 'production'
push = 'push'
reset = 'reset'

# Path to the directory where we will store the dates
path = '/Users/josephbates/scripts/pushToGithub/dates_storage'
repo_location_storage_path = '/Users/josephbates/Projects/push_to_git/repo_location_storage'
heidi_dir = '/Users/josephbates/modsy/heidi'
list_items_file_name = 'list_items.txt'

git_checkout_master = [git, checkout, master]
git_fetch_origin = [git, fetch, origin]
git_checkout_staging = [git, checkout, staging]
git_checkout_production = [git, checkout, production]
git_push_origin = [git, push, '-f', origin]

branch_prefix = {'staging': 'staging_', 'production': 'production_'}