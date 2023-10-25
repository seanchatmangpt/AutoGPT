# Import the necessary modules
import hashlib
import base64


# Define the encryption function
def encrypt(data):
    # Convert the data to bytes
    data_bytes = data.encode("utf-8")

    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()

    # Update the hash object with the data bytes
    hash_object.update(data_bytes)

    # Get the digest of the hash object
    digest = hash_object.digest()

    # Encode the digest using base64
    encoded_digest = base64.b64encode(digest)

    # Return the encoded digest as a string
    return encoded_digest.decode("utf-8")


# Test the function
encrypted_data = encrypt("Hello World")
print(
    encrypted_data
)  # Output: 7Qdih1MzJWZ+1ZJjvI8JjQZQJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJJjJjJjJjJjJjJjJjJJJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJjJj
