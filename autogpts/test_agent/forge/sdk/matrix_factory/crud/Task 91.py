# Import the necessary modules
import hashlib
import base64

# Define the encryption function
def encrypt(data):
    # Encode the data using UTF-8
    encoded_data = data.encode('utf-8')
    # Create a hash object using SHA-256 algorithm
    hash_object = hashlib.sha256()
    # Update the hash object with the encoded data
    hash_object.update(encoded_data)
    # Get the digest of the hash object
    digest = hash_object.digest()
    # Encode the digest using base64
    encoded_digest = base64.b64encode(digest)
    # Return the encoded digest
    return encoded_digest

# Define the test data
test_data = "This is a test string"

# Encrypt the test data
encrypted_data = encrypt(test_data)

# Print the encrypted data
print(encrypted_data)