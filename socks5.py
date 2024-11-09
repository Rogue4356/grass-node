# Open the file with proxies
with open('proxy.txt', 'r') as file:
    # Read all lines from the file
    proxies = file.readlines()

# Add 'http://' at the beginning of each proxy
updated_proxies = ["socks5://" + proxy.strip() for proxy in proxies]

# Write the updated proxies back to the file
with open('proxy.txt', 'w') as file:
    file.write('\n'.join(updated_proxies))

print("All proxies have been updated with 'socks5://'")
