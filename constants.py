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
dates_time_storage_path = '/push_to_git_storage/dates_storage'
repo_location_storage_path = '/push_to_git_storage/repo_location_storage'
list_items_file_name = 'list_items.txt'

git_checkout_master = [git, checkout, master]
git_fetch_origin = [git, fetch, origin]
git_checkout_staging = [git, checkout, staging]
git_checkout_production = [git, checkout, production]
git_push_origin = [git, push, '-f', origin]

branch_prefix = {'staging': 'staging_', 'production': 'production_'}

master_to_staging_str = "Master >> Staging"
staging_to_prod_str = "Staging >> Prod"
push_branch_str = " Push branch:"
stored_dir_str = "Pick a stored location: "
fetch_origin_str = "Fetch origin: "
