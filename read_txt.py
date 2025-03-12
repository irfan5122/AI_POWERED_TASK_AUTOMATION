def load_credentials(filename="data.txt"):
    credentials = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                username, password = line.strip().split(",")
                credentials[username] = password
    except FileNotFoundError:
        print("File not found.")
    return credentials

# Example usage
credentials = load_credentials("user_data.apta")
print(credentials)
print(type(credentials))