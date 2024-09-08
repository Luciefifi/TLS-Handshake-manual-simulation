import random

server_supported_tls_versions = ['TLS 1.2', 'TLS 1.3']
server_supported_cipher_suites = ['AES-256-GCM', 'CHACHA20-POLY1305']

# Function to negotiate TLS Version
def negotiate_tls_version(client_version):
    if client_version in server_supported_tls_versions:
        return client_version
    else:
        return None

# Function to select cipher suite
def select_cipher_suite(client_cipher_suite):
    if client_cipher_suite in server_supported_cipher_suites:
        return client_cipher_suite
    else:
        return None

# Function to simulate Diffie-Hellman key exchange
def diffie_hellman_key_exchange():
    # Define a prime number and base for the key exchange
    prime = 23
    base = 5

    # Generate random private keys for client and server
    client_private = random.randint(1, 10)
    server_private = random.randint(1, 10)

    # Calculate the public keys for client and server
    client_public = (base ** client_private) % prime
    server_public = (base ** server_private) % prime

    # Compute the shared secret key for client and server
    client_secret = (server_public ** client_private) % prime
    server_secret = (client_public ** server_private) % prime

    # Ensure that the computed secrets match (for correctness)
    assert client_secret == server_secret

    # Return the shared secret key
    return client_secret

# Function to display the TLS Version Menu
def choose_tls_version():
    print('\nChoose a TLS version or exit:')
    print('1. TLS 1.0')
    print('2. TLS 1.1')
    print('3. TLS 1.2')
    print('4. TLS 1.3')
    print('5. Exit')

    choice = int(input('Enter the number corresponding to your choice: '))

    tls_versions = {
        1: 'TLS 1.0',
        2: 'TLS 1.1',
        3: 'TLS 1.2',
        4: 'TLS 1.3',
        5: 'Exit'
    }

    return tls_versions.get(choice, None)

# Function to display the cipher suite menu
def choose_cipher_suite():
    print('\nChoose a Cipher suite or exit:')
    print('1. AES-128-GCM')
    print('2. AES-256-GCM')
    print('3. CHACHA20-POLY1305')
    print('4. DES-CBC3-SHA')
    print('5. Exit')

    choice = int(input('Enter the number corresponding to your choice: '))

    cipher_suites = {
        1: 'AES-128-GCM',
        2: 'AES-256-GCM',
        3: 'CHACHA20-POLY1305',
        4: 'DES-CBC3-SHA',
        5: 'Exit'
    }

    return cipher_suites.get(choice, None)

# Function to recommend switching to the latest TLS version
def recommend_latest_version(client_version):
    if client_version in server_supported_tls_versions:
        latest_version = server_supported_tls_versions[-1]  # Latest version is the last in the list
        if client_version != latest_version:
            print(f"\nYou selected {client_version}.")
            print(f"The latest supported TLS version is {latest_version}.")
            choice = input("Would you like to switch to the latest version? (yes/no): ").strip().lower()
            if choice == 'yes':
                return latest_version
    return client_version

# Main function for the handshake simulation
def tls_handshake_simulation():
    print("\nTLS HANDSHAKE SIMULATION")
    print("============================")

    # Step 1: Choose TLS Version (Client)
    client_version = choose_tls_version()
    if client_version == 'Exit':
        print("Exiting the program.")
        return  # Exit the program
    elif not client_version:
        print("Error: Invalid TLS version selected!")
        return  # Exit the program

    # Step 2: Recommending the latest version if needed
    client_version = recommend_latest_version(client_version)

    # Step 3: Server checks if it supports the chosen TLS Version
    negotiated_version = negotiate_tls_version(client_version)
    if not negotiated_version:
        print(f"Error: Server does not support TLS Version {client_version}. Handshake Failed !!!")
        return  # Exit the program

    # Step 4: Choose Cipher suite (Client)
    client_cipher_suite = choose_cipher_suite()
    if client_cipher_suite == 'Exit':
        print("Exiting the program.")
        return  # Exit the program
    elif not client_cipher_suite:
        print("Error: Invalid Cipher suite selected")
        return  # Exit the program

    # Step 5: Server checks if it supports the chosen cipher suite
    selected_cipher_suite = select_cipher_suite(client_cipher_suite)
    if not selected_cipher_suite:
        print(f"The server does not support Cipher suite {client_cipher_suite}. Handshake Failed")
        return  # Exit the program

    # Step 6: Simulating Diffie-Hellman Key Exchange and completing the handshake
    shared_secret = diffie_hellman_key_exchange()
    print("\nTLS Handshake completed successfully!")

    # Print the negotiated TLS Version and Cipher suite and generated key 
    print(f"\nThe negotiated TLS version.: {negotiated_version}")
    print(f"The negotiated Cipher Suite: {selected_cipher_suite}")
    print(f"The established shared secret key: {shared_secret}")

#  the handshake simulation
tls_handshake_simulation()
